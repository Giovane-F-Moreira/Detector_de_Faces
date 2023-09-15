import face_recognition as reconhecedor
import json

CAPTURAS_DA_CAMERA = [
    "/media/gio/Arquivos_M2/Workspace/IHM/Detector de Faces/faces/autorizados1.jpeg",
    "/media/gio/Arquivos_M2/Workspace/IHM/Detector de Faces/faces/autorizados2.jpeg",
    "/media/gio/Arquivos_M2/Workspace/IHM/Detector de Faces/faces/suspeitos1.jpeg",
    "/media/gio/Arquivos_M2/Workspace/IHM/Detector de Faces/faces/suspeitos2.jpeg"
]

ARQUIVO_DE_AUTORIZACOES = "/media/gio/Arquivos_M2/Workspace/IHM/Detector de Faces/autorizacoes.json"


def configurar():
    autorizados, suspeitos = None, None

    with open(ARQUIVO_DE_AUTORIZACOES, "r") as arquivo:
        configuracao = json.load(arquivo)
        arquivo.close()

        autorizados = configuracao["autorizados"]
        suspeitos = configuracao["suspeitos"]

    return autorizados, suspeitos


def autorizar(autorizados, visitantes):
    tem_permissoes, acessos_permitidos = False, []

    fotos_visitantes = reconhecedor.load_image_file(visitantes)
    caracteristicas_dos_visitantes = reconhecedor.face_encodings(
        fotos_visitantes)

    for autorizado in autorizados:
        foto = reconhecedor.load_image_file(autorizado["foto"])
        caracteristicas_do_autorizado = reconhecedor.face_encodings(foto)[0]

        permitido = True in reconhecedor.compare_faces(caracteristicas_dos_visitantes,
                                                       caracteristicas_do_autorizado)

        if permitido:
            acessos_permitidos.append(autorizado)

    tem_permissoes = True if len(acessos_permitidos) > 0 else False

    return tem_permissoes, acessos_permitidos


def detectar_suspeitos(suspeitos, visitantes):
    tem_suspeitos, suspeitos_detectados = False, []

    fotos_visitantes = reconhecedor.load_image_file(visitantes)
    caracteristicas_dos_visitantes = reconhecedor.face_encodings(
        fotos_visitantes)

    for suspeito in suspeitos:
        foto = reconhecedor.load_image_file(suspeito["foto"])
        caracteristicas_do_suspeito = reconhecedor.face_encodings(foto)[0]

        tem_suspeito = True in reconhecedor.compare_faces(caracteristicas_dos_visitantes,
                                                       caracteristicas_do_suspeito)

        if tem_suspeito:
            suspeitos_detectados.append(suspeito)

    tem_suspeitos = True if len(suspeitos_detectados) > 0 else False

    return tem_suspeitos, suspeitos_detectados


def imprimir_dados_dos_visitantes(visitantes):
    for visitante in visitantes:
        print(visitante['nome'])


if __name__ == "__main__":
    autorizados, suspeitos = configurar()

    for visitantes in CAPTURAS_DA_CAMERA:
        print(f"foto dos visitantes: {visitantes}")

        tem_permissoes, acessos_permitidos = autorizar(autorizados, visitantes)
        if tem_permissoes:
            print("foram reconhecidas pessoas com autorização")
            imprimir_dados_dos_visitantes(acessos_permitidos)

        tem_suspeitos, suspeitos_detectados = detectar_suspeitos(suspeitos, visitantes)
        if tem_suspeitos:
            print("foram detectados suspeitos")
            imprimir_dados_dos_visitantes(suspeitos_detectados)
