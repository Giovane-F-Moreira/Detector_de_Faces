import face_recognition as reconhecedor

FOTOS = [
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/loki1.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/loki2.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/loki3.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/loki4.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/tonho1.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/tonho2.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/tonho3.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/tonho4.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/viuva1.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/viuva2.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/viuva3.jpg",
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/viuva4.jpg"
]

CAPTURAS_DA_CAMERA = [
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/autorizados1.jpeg", 
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/autorizados2.jpeg", 
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/suspeitos1.jpeg", 
    "/misc/ifba/workspaces/ihm/reconhecimento de face/faces/suspeitos2.jpeg"
]

if __name__ == "__main__":
    for captura in CAPTURAS_DA_CAMERA:
        print(f"verificando a foto: {captura}")

        imagem_capturada = reconhecedor.load_image_file(captura)
        caracteristicas_faciais = reconhecedor.face_encodings(imagem_capturada)

        for foto in FOTOS:
            print(f"comparando com a foto: {foto}")

            foto_no_banco = reconhecedor.load_image_file(foto)
            caracteristicas_faciais_do_banco = reconhecedor.face_encodings(foto_no_banco)[0]

            resultado = reconhecedor.compare_faces(caracteristicas_faciais, caracteristicas_faciais_do_banco)

            if True in resultado:
                print("a foto foi reconhecida")
            else:
                print("a foto não foi reconhecida")