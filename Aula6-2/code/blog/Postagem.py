class Postagem:
    def __init__(self, id, titulo, texto, dataPublicacao,usuario):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.dataPublicacao = dataPublicacao
        self.usuario = usuario

    def __str__(self):
        return "id={}, titulo={}, texto={}, dataPublicacao={}, usuario.id={}".format(self.id, self.titulo, self.texto, self.dataPublicacao,self.usuario.id)