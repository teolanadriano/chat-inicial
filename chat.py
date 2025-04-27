import telebot
import os

CHAVE_API = os.getenv("CHAVE_API")

bot = telebot.TeleBot(CHAVE_API)

operadores = ['+', '-', '*', '/']

def temOperador(operacao):
    for c in operacao:
        for op in operadores:
            if c == op:
                return operacao.index(c)
    return False

@bot.message_handler(commands=['calcular'])
def calculadora(mensagem):
    operacao = mensagem.text.split()[1]

    ind_op = temOperador(operacao)
    if ind_op == False: 
        bot.reply_to(mensagem, "Não foi identificado um operador na sentença.")
        return False

    num1 = int(operacao[:ind_op])
    operador = operacao[ind_op]
    num2 = int(operacao[ind_op+1:])

    #if type(operacao[0]) == int or type(operacao[2]) == int:
    #    bot.reply_to(mensagem, "Você digitou algo que não é número.")
    #    return False
    #if operacao[1] not in operadores:
    #    bot.reply_to(mensagem, "O operador digitado não foi reconhecido.")
    #    return False
    
    #num1, operador, num2 = int(operacao[0]), operacao[1], int(operacao[2])
    
    match operador:
        case '+': bot.reply_to(mensagem, f"{operacao} = {num1+num2}")
        case '-': bot.reply_to(mensagem, f"{operacao} = {num1-num2}")
        case '*': bot.reply_to(mensagem, f"{operacao} = {num1*num2}")
        case '/': bot.reply_to(mensagem, f"{operacao} = {num1/num2}")

bot.remove_webhook()
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    msg = '''
    Digite "/calcular" e a sentença para resolver.
    '''
    bot.reply_to(mensagem, msg)

bot.polling()