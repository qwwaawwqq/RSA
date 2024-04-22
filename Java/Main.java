import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the bit length for keys (recommended 1000 or higher for testing):");
        int bitLength = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        BigInteger[] keys = RSAUtility.generateKeys(bitLength);
        BigInteger n = keys[0];
        BigInteger e = keys[1];
        BigInteger d = keys[2];

        System.out.println("Public Key: (n, e) = (" + n + ", " + e + ")");
        System.out.println("Private Key: (n, d) = (" + n + ", " + d + ")");

        System.out.println("Enter a message to encrypt:");
        String message = scanner.nextLine();

        BigInteger messageNumeric = stringToBigInteger(message);
        System.out.println("Numeric representation of message: " + messageNumeric);

        BigInteger encryptedMessage = RSAUtility.encrypt(messageNumeric, e, n);
        System.out.println("Encrypted message: " + encryptedMessage);

        BigInteger decryptedMessage = RSAUtility.decrypt(encryptedMessage, d, n);
        System.out.println("Numeric representation of decrypted message: " + decryptedMessage);

        String decryptedText = bigIntegerToString(decryptedMessage);
        System.out.println("Decrypted message: " + decryptedText);

        scanner.close();
    }

    private static BigInteger stringToBigInteger(String input) {
        return new BigInteger(1, input.getBytes());
    }

    private static String bigIntegerToString(BigInteger input) {
        return new String(input.toByteArray());
    }
}
