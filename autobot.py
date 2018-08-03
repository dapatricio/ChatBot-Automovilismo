
import json

from snips_prueba import pregunta, consulta_formula1, consulta_EquiposF1, consulta_CampeonesF1, consulta_Categorias, consulta_teamF1, consulta_CategoriasF1

import telebot
import random
import time

bot = telebot.TeleBot("613371410:AAGlohX_39XHYp1oifk4WxGgaLeDUczdYig")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("message")
    print(message)
    #bot.reply_to(message, message.text)

    chat_id = message.chat.id
    try:
        texto = message.json['text']
    except AttributeError:
        texto = "N/A"

    print("Este es el texto")
    print(texto)
    lista = ["No entendi la pregunta", "Puedes repetir la pregunta", "Indicame la pregunta nuevamente", "Dime de nuevo lo que pides", "Vuelve a ingresar tu pregunta porfavor"]
    listaError = ["Valor ingresado invalido", "El valor que ingresaste no existe", "Ingresa un valor valido por favor", "Intenta nuevamente", "No entendi el valor"]
    listaSaludo = ["Hola, como puedo ayudarte", "Hola como estas, como puedo ayudarte", "Buenos dias, como puedo ayudarte", "Hola, como puedo ayudarte", "Saludos amigo, como puedo ayudarte"]
    listaDespedida = ["Nos vemos", "Adios", "Hasta otra ocacion", "Bye, hasta otro rato", "Nos vemos amigo", "hasta otro momento"]
    listaErrorTeams = ["Quizas quisiste decir Pilotos de team Formula 1", "No querias decir los pilotos de algun team"]
    respuesta_json = pregunta(texto)
    respuesta_json = json.loads(respuesta_json)

    #print(type(respuesta_json))
    print(texto)
    respuesta_json = json.loads(pregunta(texto))
    print(pregunta(texto))
    print('\nRESPUESTA JSON: ')
    print(respuesta_json)
    try:
        if (len(respuesta_json['slots'][0]['entity'])!=1):
            intencion = respuesta_json['slots'][0]['entity'] #pilotos
            probabilidad = respuesta_json['intent']['probability']
            formula1 = respuesta_json['slots'][0]['value']['value']
            equiposf1 = respuesta_json['slots'][0]['value']['value']
            campeonesf1 = respuesta_json['slots'][0]['value']['value']
            categorias = respuesta_json['slots'][0]['value']['value']
            teamF1 = respuesta_json['slots'][0]['value']['value']
            categoriasF1 = respuesta_json['slots'][0]['value']['value']
            print("esta es la intencion:")
            print(intencion)
            print("esta es la probabilidad:")
            print(probabilidad)

            if (intencion=="formula1"):
                print("entro a pilotos:")
                print(formula1)

                lista_formula1 = consulta_formula1(formula1)
                if(len(lista_formula1)!=0 or len(formula1)!=0) :
        
                    respuesta = ""
                    lista_nombres_formula1 = []

                    for i in lista_formula1:
                        lista_nombres_formula1.append(i)
                        respuesta = respuesta + i + '\n'
                else:
                    respuesta = [random.choice(listaError)]            

            elif (intencion=="equiposf1"):
                print("entro a equipos:")
                print(equiposf1)

                lista_equiposf1 = consulta_EquiposF1(equiposf1)
                if(len(lista_equiposf1)!=0 or len(equiposf1)!=0) :
                    respuesta = ""
                    lista_nombres_campeonesf1 = []
                    respuesta = ""
                    lista_nombres_equiposf1 = []
                        
                    for i in lista_equiposf1:
                        lista_nombres_equiposf1.append(i)
                        respuesta = respuesta + i  + '\n'
                else:
                    respuesta = [random.choice(listaError)]  

            elif (intencion=="campeonesf1"):
                print("entro a campeones:")
                print(campeonesf1)

                lista_campeonesf1 = consulta_CampeonesF1(campeonesf1)
                if(len(lista_campeonesf1)!=0 or len(campeonesf1)!=0) :

                    respuesta = ""
                    lista_nombres_campeonesf1 = []
                        
                    for i in lista_campeonesf1:
                        lista_nombres_campeonesf1.append(i)
                        respuesta = respuesta + i + '\n'

                else:
                    respuesta = [random.choice(listaError)] 

            elif (intencion=="categoriasF1" and probabilidad>0.5):
                print("entro a categorias f1:")
                print(categoriasF1)

                lista_campeonesf1 = consulta_CategoriasF1(categoriasF1)
                if(len(lista_categoriasF1)!=0 or len(categoriasF1)!=0) :

                    respuesta = ""
                    lista_nombres_categoriasF1 = []
                        
                    for i in lista_categoriasF1:
                        lista_nombres_categoriasF1.append(i)
                        respuesta = respuesta + i + '\n'

                else:
                    respuesta = [random.choice(listaError)]         
            elif (intencion=="categorias"):
                print("entro a categorias:")
                print(categorias)

                lista_categorias = consulta_Categorias(categorias)
                if(len(lista_categorias)!=0 or len(categorias)!=0) :
                    respuesta = ""
                    lista_nombres_categorias = []
                        
                    for i in lista_categorias:
                        lista_nombres_categorias.append(i)
                        respuesta = respuesta + i + '\n'
                else:
                    respuesta = [random.choice(listaError)] 

            elif (intencion=="teamF1" and probabilidad>=0.7):
                print("entro a teamF1:")
                print(teamF1)

                lista_teamF1 = consulta_teamF1(teamF1)
                if(len(lista_teamF1)!=0 or len(teamF1)!=0) :
                    respuesta = ""
                    lista_nombres_teamF1 = []
                        
                    for i in lista_teamF1:
                        lista_nombres_teamF1.append(i)
                        respuesta = respuesta + i + '\n'
                else:
                    respuesta = [random.choice(listaErrorTeams)] 

            elif (intencion=="saludo"):

                respuesta = [random.choice(listaSaludo)]

            elif (intencion=="despedida"):

                respuesta = [random.choice(listaDespedida)]

            else:
                respuesta = [random.choice(lista)]
        else:
            respuesta = [random.choice(lista)]
            bot.send_message(chat_id, respuesta)
            #send_message(chat_id, text)
            
    except IndexError:
        respuesta = [random.choice(lista)]

    except:
        respuesta = [random.choice(lista)]

        ahora = time.strftime("%c")

        messageUsr = texto
        respuestaBot = str(respuesta)

        ahora = time.strftime("%c")

        file = open('ConversacionesError.txt', 'a')

        file.write("\n"+"Usuario ID:\n")
        file.write(str(chat_id)+"\n")
        file.write("\n"+ahora+": Este es el mensaje del usuario\n" + messageUsr)
        file.write("\n"+ahora +": Este es el mensaje del ChatBot\n" + respuestaBot+"\n")
        file.write("------------Separacion Mensajes--------------")

        file.close()

    messageUsr = texto
    respuestaBot = str(respuesta)

    ahora = time.strftime("%c")

    file = open('Conversaciones.txt', 'a')

    file.write("\n"+"Usuario ID:\n")
    file.write(str(chat_id)+"\n")
    file.write("\n"+ahora+": Este es el mensaje del usuario:\n" + messageUsr)
    file.write("\n"+ahora +": Este es el mensaje del ChatBot:\n" + respuestaBot+"\n")
    file.write("------------Separacion Mensajes--------------")

    file.close()

    bot.send_message(chat_id, respuesta)
    #send_message(chat_id, text)

print "Bot Iniciado =)"
bot.polling()