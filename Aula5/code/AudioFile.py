import abc

class AudioFile(abc.ABC):
    def __init__(self, filename):
        '''Isso é polimorfismo. Se o nome do arquivo não terminar com
        o extensão correta, será gerada uma exceção (esse assunto será
        tratado na próxima aula'''
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

        @abc.abstractclassmethod
        def play(self):
            pass

'''cada subclasse de AudioFile implementa o método play() de uma maneira diferente.
Isso também é polimorfismo'''

class MP3File(AudioFile): 
    ext = "mp3"
    def play(self):
        print("tocando {} como mp3".format(self.filename))

class WavFile(AudioFile): 
    ext = "wav"
    def play(self):
        print("tocando {} como wav".format(self.filename))

class OggFile(AudioFile): 
    ext = "ogg"
    def play(self):
        print("tocando {} como ogg".format(self.filename))

'''Exemplo de Duck typing'''
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename 

    def play(self):
        print("playing {} como flac".format(self.filename))


'''Pode usar exatamente o mesmo código (audio_file.play()) para 
reproduzir um arquivo de áudio, independentemente do tipo.
Não importa qual subclasse de AudioFile.'''

ogg = OggFile("myfile.ogg") 
mp3 = MP3File("myfile.mp3") 
flac = FlacFile("myfile.flac")

'''duck typing exemplo'''
for audio in [ogg, mp3, flac]:
    audio.play()

'''Raise Exception'''
not_an_mp3 = MP3File("myfile.ogg")
