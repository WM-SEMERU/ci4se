"""
Interactive DAG builder used by the causal-inference tutorial.

The notebook intentionally imports this module so the teaching material can
focus on causal assumptions, identification, estimation, and refutation.
"""

from __future__ import annotations

import copy
import math
from typing import Iterable

import networkx as nx
import ipywidgets as widgets
import seaborn as sns
from matplotlib.colors import to_hex
from IPython.display import clear_output, display

try:
    import ipycytoscape
    HAS_IPYCYTOSCAPE = True
except ImportError:
    HAS_IPYCYTOSCAPE = False


ROLE_ORDER = [
    "treatment",
    "outcome",
    "confounder",
    "mediator",
    "instrument_candidate",
    "treatment_predictor",
    "outcome_predictor",
    "collider_candidate",
    "other",
]


def infer_node_roles(
    dag: nx.DiGraph,
    treatment: str,
    outcome: str,
):
    """
    Infer descriptive roles from the DAG structure.

    The labels summarize the graph supplied by the analyst. In particular,
    "instrument candidate" is a structural hint, not proof that all
    instrumental-variable assumptions hold.
    """
    roles = {}
    explanations = {}

    ancestors_t = nx.ancestors(dag, treatment)
    ancestors_y = nx.ancestors(dag, outcome)
    descendants_t = nx.descendants(dag, treatment)

    dag_without_t = dag.copy()
    if treatment in dag_without_t:
        dag_without_t.remove_node(treatment)

    for node in dag.nodes:
        reasons = []

        if node == treatment:
            role = "treatment"
            reasons.append("configured treatment node")

        elif node == outcome:
            role = "outcome"
            reasons.append("configured outcome node")

        elif node in descendants_t and node in ancestors_y:
            role = "mediator"
            reasons.extend([
                "descendant of treatment",
                "ancestor of outcome",
            ])

        elif node in ancestors_t:
            # A pre-treatment ancestor of treatment is a common-cause candidate
            # only if it can still reach outcome after treatment is removed.
            has_path_to_y_without_t = (
                node in dag_without_t
                and outcome in dag_without_t
                and nx.has_path(dag_without_t, node, outcome)
            )

            if has_path_to_y_without_t:
                role = "confounder"
                reasons.extend([
                    "ancestor of treatment",
                    "directed path to outcome remains after treatment is removed",
                ])
            else:
                role = "instrument_candidate"
                reasons.extend([
                    "ancestor of treatment",
                    "no directed path to outcome remains after treatment is removed",
                ])

        elif node in ancestors_y:
            role = "outcome_predictor"
            reasons.extend([
                "ancestor of outcome",
                "not an ancestor of treatment",
            ])

        elif dag.in_degree(node) >= 2:
            role = "collider_candidate"
            reasons.extend([
                f"{dag.in_degree(node)} incoming causal arrows",
                "structural collider candidate",
            ])

        else:
            role = "other"
            reasons.append("no special treatment–outcome role inferred")

        roles[node] = role
        explanations[node] = reasons

    return roles, explanations


def validate_dag(
    dag: nx.DiGraph,
    data_columns: Iterable[str],
    treatment: str,
    outcome: str,
) -> None:
    """Validate the graph before passing it to DoWhy."""
    if not isinstance(dag, nx.DiGraph):
        raise TypeError("The causal graph must be a networkx.DiGraph.")

    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError("The causal graph must be acyclic.")

    unknown = sorted(set(dag.nodes) - set(data_columns))
    if unknown:
        raise ValueError(f"Graph nodes are missing from the dataset: {unknown}")

    for node in (treatment, outcome):
        if node not in dag:
            raise ValueError(f"Required graph node is missing: {node}")

    if not nx.has_path(dag, treatment, outcome):
        raise ValueError(
            f"No directed path exists from treatment '{treatment}' "
            f"to outcome '{outcome}'."
        )


def graph_to_dot(graph: nx.DiGraph) -> str:
    lines = ["digraph {"]
    for node in graph.nodes:
        lines.append(f'    "{node}";')
    for source, target in graph.edges:
        lines.append(f'    "{source}" -> "{target}";')
    lines.append("}")
    return "\n".join(lines)


def graph_to_gml(graph: nx.DiGraph) -> str:
    return "\n".join(nx.generate_gml(graph))


def _srgb_to_linear(channel: float) -> float:
    channel = float(channel)
    return (
        channel / 12.92
        if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
    )


def _rgb_to_xyz(rgb):
    r, g, b = (_srgb_to_linear(c) for c in rgb)
    return (
        0.4124564 * r + 0.3575761 * g + 0.1804375 * b,
        0.2126729 * r + 0.7151522 * g + 0.0721750 * b,
        0.0193339 * r + 0.1191920 * g + 0.9503041 * b,
    )


def _xyz_to_lab(xyz):
    x, y, z = xyz
    xr, yr, zr = x / 0.95047, y / 1.0, z / 1.08883

    def f(value):
        delta = 6 / 29
        return (
            value ** (1 / 3)
            if value > delta ** 3
            else value / (3 * delta ** 2) + 4 / 29
        )

    fx, fy, fz = f(xr), f(yr), f(zr)
    return (
        116 * fy - 16,
        500 * (fx - fy),
        200 * (fy - fz),
    )


def _lab_distance(rgb1, rgb2) -> float:
    lab1 = _xyz_to_lab(_rgb_to_xyz(rgb1))
    lab2 = _xyz_to_lab(_rgb_to_xyz(rgb2))
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(lab1, lab2)))


def _distinct_palette(palette_name: str, n_colors: int, candidate_count: int = 72):
    """Choose distinct colors from a Seaborn palette.

    Categorical palettes such as ``colorblind`` already contain deliberately
    separated colors, so they are used directly. Continuous palettes are
    sampled densely and reduced using perceptual distance.
    """
    categorical_palettes = {
        "colorblind",
        "deep",
        "muted",
        "bright",
        "pastel",
        "dark",
        "Set1",
        "Set2",
        "Set3",
        "tab10",
        "tab20",
    }

    try:
        if palette_name in categorical_palettes:
            return list(sns.color_palette(palette_name, n_colors=n_colors))

        candidates = list(
            sns.color_palette(
                palette_name,
                n_colors=max(candidate_count, n_colors),
            )
        )
    except Exception as exc:
        raise ValueError(
            f"Unknown or unsupported Seaborn palette: {palette_name!r}"
        ) from exc

    labs = [_xyz_to_lab(_rgb_to_xyz(rgb)) for rgb in candidates]
    darkest = min(range(len(candidates)), key=lambda i: labs[i][0])
    lightest = max(range(len(candidates)), key=lambda i: labs[i][0])

    selected = [darkest]
    if n_colors > 1 and lightest != darkest:
        selected.append(lightest)

    while len(selected) < n_colors:
        remaining = [i for i in range(len(candidates)) if i not in selected]

        def nearest_selected_distance(i):
            return min(
                _lab_distance(candidates[i], candidates[j])
                for j in selected
            )

        selected.append(
            max(
                remaining,
                key=lambda i: (nearest_selected_distance(i), -i),
            )
        )

    selected = sorted(selected[:n_colors])
    return [candidates[i] for i in selected]


class CausalGraphBuilder:
    """Notebook-friendly interactive DAG builder."""

    def __init__(
        self,
        data_columns: Iterable[str],
        treatment: str,
        outcome: str,
        covariates: Iterable[str] | None = None,
        palette: str = "colorblind",
        edge_opacity: float = 0.35,
    ):
        self.data_columns = list(data_columns)
        self.treatment = treatment
        self.outcome = outcome
        self.covariates = list(covariates or [])
        self.graph_variables = list(
            dict.fromkeys([treatment, outcome, *self.covariates])
        )

        missing = sorted(set(self.graph_variables) - set(self.data_columns))
        if missing:
            raise ValueError(
                f"Graph variables are missing from the dataset: {missing}"
            )

        self.palette_name = palette
        self.edge_opacity = min(max(float(edge_opacity), 0.0), 1.0)

        colors = _distinct_palette(
            self.palette_name,
            n_colors=len(ROLE_ORDER),
        )
        self.role_colors = {
            role: to_hex(color)
            for role, color in zip(ROLE_ORDER, colors)
        }

        self.dag = nx.DiGraph()
        self.dag.add_nodes_from(self.graph_variables)
        self.dag.add_edge(self.treatment, self.outcome)

        self.roles = {}
        self.role_explanations = {}
        self._frozen_dag = None
        self.selected_source = None
        self.selected_target = None
        self.selected_edge = None

        self._build_controls()
        self._refresh_roles()

    def _tutorial_edges(self):
        edges = [(self.treatment, self.outcome)]
        for covariate in self.covariates:
            edges.extend([
                (covariate, self.treatment),
                (covariate, self.outcome),
            ])
        return edges

    def _refresh_roles(self):
        self.roles, self.role_explanations = infer_node_roles(
            self.dag,
            self.treatment,
            self.outcome,
        )

    def _node_color(self, node):
        return self.role_colors.get(
            self.roles.get(node, "other"),
            self.role_colors["other"],
        )

    def _safe_html(self, value):
        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    def _build_controls(self):
        self.layout_dropdown = widgets.Dropdown(
            options=[
                ("Hierarchical", "breadthfirst"),
                ("Force directed", "cose"),
                ("Circle", "circle"),
                ("Grid", "grid"),
            ],
            value="breadthfirst",
            description="Layout:",
            layout=widgets.Layout(width="260px"),
        )

        options = [("—", None)] + [(v, v) for v in self.graph_variables]
        self.source_dropdown = widgets.Dropdown(
            options=options,
            description="Source:",
            layout=widgets.Layout(width="46%"),
        )
        self.target_dropdown = widgets.Dropdown(
            options=options,
            description="Target:",
            layout=widgets.Layout(width="46%"),
        )

        self.add_edge_button = widgets.Button(
            description="Add selected edge",
            button_style="success",
            icon="plus",
        )
        self.remove_edge_button = widgets.Button(
            description="Remove selected edge",
            button_style="warning",
            icon="minus",
        )
        self.tutorial_button = widgets.Button(
            description="Common-cause template",
            icon="sitemap",
        )
        self.minimal_button = widgets.Button(
            description="Reset to T → Y",
            icon="long-arrow-right",
        )
        self.clear_button = widgets.Button(
            description="Clear edges",
            icon="trash",
        )
        self.freeze_button = widgets.Button(
            description="Use this DAG for analysis",
            button_style="primary",
            icon="check",
        )

        self.selection_html = widgets.HTML()
        self.diagnostics_html = widgets.HTML()
        self.status_html = widgets.HTML()
        self.graph_output = widgets.Output()
        self.export_output = widgets.Output()

        self.source_dropdown.observe(
            self._sync_dropdown_selection,
            names="value",
        )
        self.target_dropdown.observe(
            self._sync_dropdown_selection,
            names="value",
        )
        self.layout_dropdown.observe(
            self._change_layout,
            names="value",
        )

        self.add_edge_button.on_click(self._add_selected_edge)
        self.remove_edge_button.on_click(self._remove_selected_edge)
        self.tutorial_button.on_click(self._load_tutorial)
        self.minimal_button.on_click(self._load_minimal)
        self.clear_button.on_click(self._clear_edges)
        self.freeze_button.on_click(self._freeze_graph)

    def _set_status(self, message, kind="info"):
        palette = {
            "info": ("#eef4ff", "#244a7c"),
            "success": ("#ecf8f0", "#1d6334"),
            "warning": ("#fff7e6", "#76520b"),
            "error": ("#fdeeee", "#8b2e2e"),
        }
        bg, fg = palette.get(kind, palette["info"])
        self.status_html.value = (
            f'<div style="font-family:system-ui,sans-serif;'
            f'background:{bg};color:{fg};padding:9px 12px;'
            f'border-radius:9px;margin-top:8px;">'
            f'{self._safe_html(message)}</div>'
        )

    def _update_selection_display(self):
        self._refresh_roles()
        src = self._safe_html(self.selected_source) if self.selected_source else "—"
        tgt = self._safe_html(self.selected_target) if self.selected_target else "—"
        edge = (
            f"{self._safe_html(self.selected_edge[0])} → "
            f"{self._safe_html(self.selected_edge[1])}"
            if self.selected_edge else "—"
        )

        selected_node = self.selected_source or self.selected_target
        role_html = ""

        if selected_node:
            role = self.roles.get(selected_node, "other")
            reasons = self.role_explanations.get(selected_node, [])
            reasons_html = "".join(
                f"<li>{self._safe_html(reason)}</li>"
                for reason in reasons
            )
            role_html = (
                '<div style="margin-top:8px;padding-top:8px;'
                'border-top:1px solid #e5e7eb;">'
                f'<div><b>Inferred role:</b> '
                f'<code>{self._safe_html(role)}</code></div>'
                f'<ul style="margin:6px 0 0 20px;">{reasons_html}</ul>'
                '</div>'
            )

        self.selection_html.value = (
            '<div style="font-family:system-ui,sans-serif;'
            'padding:10px 12px;border:1px solid #ddd;'
            'border-radius:10px;margin:8px 0;">'
            '<b>Selection</b>'
            f'<span style="margin-left:16px;">Source: <code>{src}</code></span>'
            f'<span style="margin-left:16px;">Target: <code>{tgt}</code></span>'
            f'<span style="margin-left:16px;">Edge: <code>{edge}</code></span>'
            f'{role_html}</div>'
        )

    def _update_diagnostics(self):
        self._refresh_roles()
        valid = nx.is_directed_acyclic_graph(self.dag)
        has_path = nx.has_path(self.dag, self.treatment, self.outcome)

        common_ancestors = (
            nx.ancestors(self.dag, self.treatment)
            & nx.ancestors(self.dag, self.outcome)
        )
        pathway_nodes = (
            nx.descendants(self.dag, self.treatment)
            & nx.ancestors(self.dag, self.outcome)
        ) - {self.outcome}

        role_counts = {}
        for role in self.roles.values():
            role_counts[role] = role_counts.get(role, 0) + 1

        role_summary = ", ".join(
            f"{role}: {count}"
            for role, count in sorted(role_counts.items())
            if role not in {"treatment", "outcome"}
        ) or "none"

        self.diagnostics_html.value = (
            '<div style="display:grid;grid-template-columns:'
            'repeat(2,minmax(0,1fr));gap:8px;'
            'font-family:system-ui,sans-serif;margin-top:8px;">'
            '<div style="padding:10px;border:1px solid #ddd;border-radius:10px;">'
            '<div style="font-size:12px;color:#666;">Graph status</div>'
            f'<div style="font-weight:700;">{"✓" if valid else "✗"} '
            f'{"Valid DAG" if valid else "Invalid graph"}</div></div>'
            '<div style="padding:10px;border:1px solid #ddd;border-radius:10px;">'
            '<div style="font-size:12px;color:#666;">Treatment → outcome path</div>'
            f'<div style="font-weight:700;">{"✓ Present" if has_path else "✗ Missing"}</div></div>'
            '<div style="padding:10px;border:1px solid #ddd;border-radius:10px;">'
            '<div style="font-size:12px;color:#666;">Nodes / edges</div>'
            f'<div style="font-weight:700;">{self.dag.number_of_nodes()} / '
            f'{self.dag.number_of_edges()}</div></div>'
            '<div style="padding:10px;border:1px solid #ddd;border-radius:10px;">'
            '<div style="font-size:12px;color:#666;">Common ancestors</div>'
            f'<div style="font-weight:700;">{len(common_ancestors)}</div></div>'
            '</div>'
            '<div style="font-family:system-ui,sans-serif;'
            'font-size:12px;color:#666;margin-top:8px;">'
            'Treatment→outcome pathway nodes: '
            f'<b>{self._safe_html(", ".join(sorted(pathway_nodes)) or "none")}</b><br>'
            'Inferred roles: '
            f'<b>{self._safe_html(role_summary)}</b></div>'
        )

    def _cytoscape_json(self):
        self._refresh_roles()
        nodes = [
            {
                "data": {
                    "id": node,
                    "label": node,
                    "role": self.roles.get(node, "other"),
                    "nodeColor": self._node_color(node),
                }
            }
            for node in self.dag.nodes
        ]

        edges = []
        for source, target in self.dag.edges:
            edge_class = (
                "effect-edge"
                if source == self.treatment and target == self.outcome
                else "structural-edge"
            )
            edges.append({
                "data": {
                    "id": f"{source}__TO__{target}",
                    "source": source,
                    "target": target,
                    "edgeColor": self._node_color(source),
                    "edgeOpacity": self.edge_opacity,
                },
                "classes": edge_class,
            })

        return {"nodes": nodes, "edges": edges}

    def _cyto_style(self):
        return [
            {
                "selector": "node",
                "style": {
                    "label": "data(label)",
                    "font-size": "12px",
                    "font-family": "system-ui, sans-serif",
                    "font-weight": "600",
                    "text-wrap": "wrap",
                    "text-max-width": "145px",
                    "text-valign": "center",
                    "text-halign": "center",
                    "color": "#ffffff",
                    "shape": "round-rectangle",
                    "width": "165px",
                    "height": "54px",
                    "padding": "8px",
                    "border-width": "2px",
                    "border-color": "#ffffff",
                    "background-color": "data(nodeColor)",
                },
            },
            {
                "selector": 'node[role = "treatment"]',
                "style": {
                    "width": "145px",
                    "height": "58px",
                    "font-size": "13px",
                    "font-weight": "700",
                    "border-width": "3px",
                },
            },
            {
                "selector": 'node[role = "outcome"]',
                "style": {
                    "width": "145px",
                    "height": "58px",
                    "font-size": "13px",
                    "font-weight": "700",
                    "border-width": "3px",
                },
            },
            {
                "selector": 'node[role = "mediator"]',
                "style": {"shape": "diamond"},
            },
            {
                "selector": 'node[role = "instrument_candidate"]',
                "style": {"shape": "hexagon"},
            },
            {
                "selector": 'node[role = "collider_candidate"]',
                "style": {"shape": "vee"},
            },
            {
                "selector": "edge",
                "style": {
                    "curve-style": "bezier",
                    "width": "3px",
                    "opacity": "data(edgeOpacity)",
                    "line-color": "data(edgeColor)",
                    "target-arrow-color": "data(edgeColor)",
                    "target-arrow-shape": "triangle",
                    "arrow-scale": 1.25,
                },
            },
            {
                "selector": ".effect-edge",
                "style": {
                    "width": "5px",
                    "opacity": 0.9,
                },
            },
            {
                "selector": ":selected",
                "style": {
                    "border-width": "5px",
                    "border-color": "#111827",
                    "line-color": "#111827",
                    "target-arrow-color": "#111827",
                    "opacity": 1.0,
                },
            },
        ]

    def _handle_node_click(self, node):
        node_id = node.get("data", {}).get("id")
        if not node_id:
            return

        if self.selected_source is None or self.selected_target is not None:
            self.selected_source = node_id
            self.selected_target = None
        elif node_id == self.selected_source:
            self.selected_source = None
        else:
            self.selected_target = node_id

        self.source_dropdown.value = self.selected_source
        self.target_dropdown.value = self.selected_target
        self._update_selection_display()

    def _handle_edge_click(self, edge):
        data = edge.get("data", {})
        source, target = data.get("source"), data.get("target")
        if source and target:
            self.selected_edge = (source, target)
            self._update_selection_display()

    def _render_graph(self):
        self._update_diagnostics()
        self._update_selection_display()

        with self.graph_output:
            clear_output(wait=True)

            if HAS_IPYCYTOSCAPE:
                cyto = ipycytoscape.CytoscapeWidget()
                cyto.graph.add_graph_from_json(
                    self._cytoscape_json(),
                    directed=True,
                )
                cyto.set_style(self._cyto_style())
                cyto.set_layout(
                    name=self.layout_dropdown.value,
                    directed=True,
                    padding=30,
                    spacingFactor=1.55,
                    animate=False,
                )
                cyto.layout.height = "560px"
                cyto.layout.width = "100%"
                cyto.user_zooming_enabled = True
                cyto.user_panning_enabled = True
                cyto.auto_ungrabify = False
                cyto.on("node", "click", self._handle_node_click)
                cyto.on("edge", "click", self._handle_edge_click)
                display(cyto)
            else:
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(12, 7))
                positions = nx.spring_layout(self.dag, seed=42, k=1.2)
                nx.draw_networkx(
                    self.dag,
                    positions,
                    node_color=[self._node_color(n) for n in self.dag.nodes],
                    edge_color=[self._node_color(s) for s, _ in self.dag.edges],
                    node_size=1900,
                    font_size=8,
                    font_color="white",
                    arrows=True,
                    arrowsize=20,
                    width=2.2,
                    alpha=0.95,
                    ax=ax,
                )
                ax.axis("off")
                plt.show()

    def _sync_dropdown_selection(self, _=None):
        self.selected_source = self.source_dropdown.value
        self.selected_target = self.target_dropdown.value
        self._update_selection_display()

    def _add_selected_edge(self, _):
        source = self.source_dropdown.value
        target = self.target_dropdown.value

        if source is None or target is None:
            self._set_status("Select both a source and a target node.", "warning")
            return
        if source == target:
            self._set_status("Self-loops are not allowed.", "error")
            return
        if self.dag.has_edge(source, target):
            self._set_status(f"Edge already exists: {source} → {target}", "info")
            return

        self.dag.add_edge(source, target)
        if not nx.is_directed_acyclic_graph(self.dag):
            self.dag.remove_edge(source, target)
            self._set_status(
                f"Rejected {source} → {target}: it would create a cycle.",
                "error",
            )
            return

        self.selected_edge = (source, target)
        self._set_status(f"Added edge: {source} → {target}", "success")
        self._render_graph()

    def _remove_selected_edge(self, _):
        if self.selected_edge is None:
            source = self.source_dropdown.value
            target = self.target_dropdown.value
            if (
                source is not None
                and target is not None
                and self.dag.has_edge(source, target)
            ):
                self.selected_edge = (source, target)

        if (
            self.selected_edge is None
            or not self.dag.has_edge(*self.selected_edge)
        ):
            self._set_status(
                "Click an edge, or select its source and target first.",
                "warning",
            )
            return

        removed = self.selected_edge
        self.dag.remove_edge(*removed)
        self.selected_edge = None
        self._set_status(
            f"Removed edge: {removed[0]} → {removed[1]}",
            "success",
        )
        self._render_graph()

    def _load_tutorial(self, _):
        self.dag.remove_edges_from(list(self.dag.edges()))
        self.dag.add_edges_from(self._tutorial_edges())
        self.selected_edge = None
        self._set_status(
            "Loaded the common-cause template. It treats every varying "
            "covariate as a cause of both treatment and outcome; review "
            "each edge before using it.",
            "warning",
        )
        self._render_graph()

    def _load_minimal(self, _):
        self.dag.remove_edges_from(list(self.dag.edges()))
        self.dag.add_edge(self.treatment, self.outcome)
        self.selected_edge = None
        self._set_status("Reset to the minimal treatment → outcome DAG.", "success")
        self._render_graph()

    def _clear_edges(self, _):
        self.dag.remove_edges_from(list(self.dag.edges()))
        self.selected_edge = None
        self._set_status("Cleared all graph edges.", "info")
        self._render_graph()

    def _change_layout(self, change):
        if change.get("name") == "value":
            self._render_graph()

    def _freeze_graph(self, _):
        try:
            validate_dag(
                self.dag,
                self.data_columns,
                self.treatment,
                self.outcome,
            )
        except Exception as exc:
            self._set_status(str(exc), "error")
            return

        self._frozen_dag = copy.deepcopy(self.dag)
        self._set_status(
            f"DAG frozen for analysis: {self._frozen_dag.number_of_nodes()} "
            f"nodes, {self._frozen_dag.number_of_edges()} edges.",
            "success",
        )

        with self.export_output:
            clear_output(wait=True)
            print("GML representation:\n")
            print(graph_to_gml(self._frozen_dag))
            print("\nDOT representation:\n")
            print(graph_to_dot(self._frozen_dag))

    def _legend(self):
        badges = []
        for role in ROLE_ORDER:
            if role == "other":
                continue
            label = role.replace("_", " ").title()
            badges.append(
                f'<span style="padding:3px 8px;border-radius:999px;'
                f'background:{self.role_colors[role]};color:white;'
                f'font-size:12px;font-weight:700;">{label}</span>'
            )

        return widgets.HTML(
            '<div style="font-family:system-ui,sans-serif;margin-bottom:8px;">'
            '<div style="display:flex;flex-wrap:wrap;gap:8px;'
            'align-items:center;margin-bottom:6px;">'
            '<span style="font-weight:700;">Causal graph workspace</span>'
            + "".join(badges)
            + '</div>'
            '<div style="display:flex;flex-wrap:wrap;gap:14px;'
            'font-size:12px;color:#475569;">'
            f'<span>Palette: <b>{self._safe_html(self.palette_name)}</b></span>'
            f'<span>Edge opacity: <b>{self.edge_opacity:.2f}</b></span>'
            '<span>Roles are inferred from DAG structure.</span>'
            '<span>Edges inherit the color of their source node.</span>'
            '</div></div>'
        )

    def display(self):
        """Render the graph editor in the notebook."""
        workspace = widgets.VBox([
            self._legend(),
            widgets.HBox([
                self.layout_dropdown,
                self.tutorial_button,
                self.minimal_button,
                self.clear_button,
            ]),
            self.selection_html,
            widgets.HBox([
                self.source_dropdown,
                self.target_dropdown,
            ]),
            widgets.HBox([
                self.add_edge_button,
                self.remove_edge_button,
            ]),
            self.graph_output,
            self.diagnostics_html,
            self.status_html,
            widgets.HBox([self.freeze_button]),
        ])

        accordion = widgets.Accordion(children=[self.export_output])
        accordion.set_title(0, "Graph export")

        display(workspace)
        display(accordion)

        self._set_status(
            "Minimal treatment → outcome DAG loaded. Use the DAG worksheet and domain "
            "knowledge to add justified edges, then click "
            "“Use this DAG for analysis”.",
            "info",
        )
        self._render_graph()

    def get_frozen_graph(self) -> nx.DiGraph:
        """Return a copy of the DAG frozen with the UI button."""
        if self._frozen_dag is None:
            raise RuntimeError(
                "No DAG has been frozen. Click 'Use this DAG for analysis' "
                "in the graph workspace first."
            )

        validate_dag(
            self._frozen_dag,
            self.data_columns,
            self.treatment,
            self.outcome,
        )
        return copy.deepcopy(self._frozen_dag)
