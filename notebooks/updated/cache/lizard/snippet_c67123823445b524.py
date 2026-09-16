def new_table_graphicFrame(cls, id_, name, rows, cols, x, y, cx, cy):
    graphicFrame = cls.new_graphicFrame(id_, name, x, y, cx, cy)
    graphicFrame.graphic.graphicData.uri = GRAPHIC_DATA_URI_TABLE
    graphicFrame.graphic.graphicData.append(CT_Table.new_tbl(rows, cols, cx,
        cy))
    return graphicFrame