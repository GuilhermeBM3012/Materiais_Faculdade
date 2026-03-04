import java.util.Scanner;

public class ex02 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        int valor1, valor2;

        System.out.println("Digite um valor positivo: ");
        valor1 = ler.nextInt();

        System.out.println("Digite um valor positivo: ");
        valor2 = ler.nextInt();

        while(valor2 <= valor1){
            System.out.printf("O 2º valor (%d) tem que ser maior que o 1º (%d)", valor2, valor1);
            valor2 = ler.nextInt();

            if(valor2 > valor1)
                    break;
        }

        ler.close();
    }
}
