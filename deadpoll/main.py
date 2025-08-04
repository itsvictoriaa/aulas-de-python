def main():
     idade = int(input ("digite a sua idade"))
     if idade >= 18:
           print("vc pode entrar")
     elif idade >=16:
          acompanhante= input("voce esta acompanhado")
          if acompanhante == "s":
               print("voce pode entrar")
          else:    
            print("voce pode entrar")
     else:
        print("vc n pode entrar")

            
     return 0 
main()

