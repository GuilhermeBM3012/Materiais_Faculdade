import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        int num, multipliador, resultado;

        System.out.println("Digite um valor positivo: ");
        num = ler.nextInt();

        while(num <= 0){
            System.out.println("Não aceita nº negativo ou o zero!");
            System.out.println("Digite um valor positivo: ");
            num = ler.nextInt();
        }

        multipliador = 1;
        while(multipliador <= 10){
            resultado = num * multipliador;
            System.out.printf("%.d X %.d = %.d", num, multipliador, resultado);

            multipliador ++;
        }
        /*for(multipliador = 1; multipliador <= 10; multipliador ++){
            resultado = num * multipliador;
            System.out.printf("%.d X %.d = %.d", num, multipliador, resultado);
        }*/

        ler.close();
    }
}
