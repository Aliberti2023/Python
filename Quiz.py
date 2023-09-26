print("Copa do Mundo?")
answer_user = input("quer começar? (S/N)")

if answer_user != "S":
     quit()

Score = 0

print("começando...")
print("Quantos Titulos o Brasil conquistou?\n (A) 3 \n (B) 4\n (C) 5\n (D) 6\n")
answer_1 = input("Resposta:")

if answer_1 == "C":
    print("Correto!")
    Score = Score + 1
else:
     print("Incorreto")  

print("Qual o Ultimo Campeão da Copa?\n (A) França \n (B) Brasil\n (C) Alemanha\n (D) Argentina\n")
answer_1 = input("Resposta:")

if answer_1 == "D":
    print("Correto!")
    Score = Score + 1
else:
     print("Incorreto")

print("Quem foi o Artilheiro da ultima copa?\n (A) Julián Álvarez \n (B) Messi\n (C) Mbappé\n (D) Richarlison\n")
answer_1 = input("Resposta:")

if answer_1 == "C":
    print("Correto!")
    Score = Score + 1
else:
     print("Incorreto")

print(f"Quiz Acabou...Pontuação: {Score}/3")    

