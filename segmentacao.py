import numpy as np
import cv2 
import matplotlib.pyplot as plt

click = []
clicked = False

def click_event(event, x, y, flags, params): 
    global click, clicked
    
    if event == cv2.EVENT_LBUTTONDOWN and not clicked: 
      print(x, ' ', y) 
      font = cv2.FONT_HERSHEY_SIMPLEX 
      cv2.putText(params, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
      cv2.imshow('image', params) 
      click = [x, y]
      clicked = True


def setup_click_event(image_path):
    global click, clicked
    click = []  
    clicked = False

    img = cv2.imread(image_path, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event, img)

    while not clicked:
        cv2.waitKey(1)
        
    cv2.destroyAllWindows()

    return click
    

def on_trackbar(val):
    global limiar
    limiar = val
    cv2.setTrackbarPos('Limiar', 'Região de Interesse', limiar)


def limiar_func(img_dir, limiar_init=4000):
    global limiar
    limiar = limiar_init

    x1 = 0
    x2 = 1280
    y1 = 0
    y2 = 0

    rec_img = []

    img = cv2.imread(img_dir, cv2.IMREAD_ANYDEPTH)
    img_np = np.asanyarray(img, dtype=np.uint16)

    cv2.imshow("Imagem de profundidade", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Roda a imagem até esta devidamente recortada na linha desejada
    while True:

        _, y2 = setup_click_event(img_dir)
        if (y2 - 170 > 0): y1 = y2 - 170 
        else: y1 = 0

        rec_img = img_np[y1:y2, x1:x2]

        plt.imshow(rec_img, cmap='gray')
        plt.title("Imagem Recortada")
        plt.show()

        quest = input("A imagem está corretamente dividida? (s ou n) ")
        if quest == 's': break

    
    cv2.namedWindow("Região de Interesse")
    cv2.createTrackbar("Limiar", "Região de Interesse", limiar, 65535, on_trackbar)

    while True:
        
        img_lmr = np.where(rec_img > limiar, 1, 0).astype(np.uint16) * 65535
        
        img_lmr_norm = cv2.normalize(img_lmr, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        # Mostrar a imagem limiarizada
        cv2.imshow("Região de Interesse", img_lmr_norm)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # Pressione 'Esc' para sair do loop
            break
        elif k == ord('e'): # Pressione "e" se quiser digitar o valor do limiar
            limiar = int(input("Digite o valor do limiar: "))
            on_trackbar(limiar)


    contours_bot, hierarchy = cv2.findContours(img_lmr_norm, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)

    boxes = []
    for i in range(len(contours_bot)):
        if 30 < len(contours_bot[i]) < 200:
            x, y, w, h = cv2.boundingRect(contours_bot[i])

            y += y1

            boxes.append((x, y, w, h))

    boxes_sort = sorted(boxes, key=lambda box: box[0])

    num = int(input("Digite o número do primeiro ovo: "))
    for (x, y, w, h) in boxes_sort:
        
        countour_area = img[y:y+h, x:x+w]
        img_display = img.copy()
        cv2.rectangle(img_display, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(x, y), (x+w, y+h)

        ###Configurações para exclusão de áreas irrelevantes (muito pequenas ou muito grande)
        #Para imagens com resolução 1280 x 720
        min_high = 80
        max_high = 170

        #Para imagens com resolução 640 x 480
        min_low = 50
        max_low = 150
        # Trocar variáveis a depender da resolução
        if max_high > w > min_high and max_high > h > min_high:
            cv2.imwrite(f"ovo{num}.png", countour_area)
            num += 3

        cv2.imshow("Recorte dos ovos", img_display)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#Roda a função para as três linhas da bandeja de ovos
for i in range(3):
    limiar_func(img_dir="Imagens_28dias_novo\Foto14.png")

#Roda a função para apenas uma linha desejada da bandeja 
# limiar_func(img_dir="Imagens_28dias_novo\Foto1.png")