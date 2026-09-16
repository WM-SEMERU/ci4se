def inserir(self, id_grupo_usuario, id_grupo_equipamento, leitura, escrita,
    alterar_config, exclusao):
    direito_map = dict()
    direito_map['id_grupo_usuario'] = id_grupo_usuario
    direito_map['id_grupo_equipamento'] = id_grupo_equipamento
    direito_map['leitura'] = leitura
    direito_map['escrita'] = escrita
    direito_map['alterar_config'] = alterar_config
    direito_map['exclusao'] = exclusao
    code, xml = self.submit({'direito_grupo_equipamento': direito_map},
        'POST', 'direitosgrupoequipamento/')
    return self.response(code, xml)