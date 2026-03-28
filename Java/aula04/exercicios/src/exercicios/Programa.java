package exercicios;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        Cliente[] lista_cliente = new Cliente[5];
        
        for (int i = 0; i < 5; i++){
            Cliente c = new Cliente();
            
            System.out.printf("Diga o nome do %dº cliente: ", i);
            c.nome = ler.next();

            System.out.printf("Diga a idade do %d cliente: ", i);
            c.idade = ler.nextInt();

            System.out.printf("Diga o email do %d cliente : ", i);
            c.email = ler.next();

            lista_cliente[i] = c;
        }

        System.out.println("\n--- LISTA DE CLIENTES ---");
        for (int i = 0; i < 5; i++){
            Cliente c = lista_cliente[i];

            if (c.idade > 18)
                System.out.printf("ID: %d\nNome: %s\nIdade: %d\n" +
                            "Email: %s\n", c.id, c.nome, c.idade, c.email);
        }
        ler.close()
    }
}
