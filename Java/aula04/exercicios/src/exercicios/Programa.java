package exercicios;

import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        for (int i = 1; i <= 5; i++){
            Clientes c = new Clientes();

            c.id = i;
            System.out.printf("Diga o nome do %dº cliente: ", i);
            c.nome = ler.next();

            System.out.printf("Diga a idade do %d cliente: ", i);
            c.idade = ler.nextInt();

            System.out.printf("Diga o email do %d cliente : ", i);
            c.email = ler.next();

            c.id ++;

            System.out.printf("ID: %d\nNome:%s\nIdade: %d\n" +
                    "Email:%s\n", c.id, c.nome, c.idade, c.email);
        }
    }
}
