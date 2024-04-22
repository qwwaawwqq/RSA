import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Scanner;

public class RSAUtility {
    private static final SecureRandom random = new SecureRandom();

    // Function to find the greatest common divisor
    public static BigInteger gcd(BigInteger a, BigInteger b) {
        return a.gcd(b);
    }

    // Function to perform exponentiation
    public static BigInteger pow(BigInteger base, BigInteger exponent, BigInteger modulus) {
        return base.modPow(exponent, modulus);
    }

    // Function to perform modulo operation
    public static BigInteger modulo(BigInteger a, BigInteger b) {
        return a.mod(b);
    }

    // Function for all calculations related to the public key exponent
    public static BigInteger cpubexp(BigInteger phi, int bitLength) {
        BigInteger e = BigInteger.probablePrime(bitLength / 2, random);
        while (!gcd(e, phi).equals(BigInteger.ONE)) {
            e = e.add(BigInteger.TWO);
        }
        return e;
    }

    // Function for all calculations related to the private key exponent
    public static BigInteger cprivexp(BigInteger e, BigInteger phi) {
        return e.modInverse(phi);
    }

    // Function to generate RSA keys
    public static BigInteger[] generateKeys(int bitLength) {
        BigInteger p = BigInteger.probablePrime(bitLength / 2, random);
        BigInteger q = BigInteger.probablePrime(bitLength / 2, random);
        BigInteger n = p.multiply(q);
        BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
        BigInteger e = cpubexp(phi, bitLength);
        BigInteger d = cprivexp(e, phi);
        return new BigInteger[]{n, e, d};
    }

    // Function to perform encryption
    public static BigInteger encrypt(BigInteger message, BigInteger e, BigInteger n) {
        return pow(message, e, n);
    }

    // Function to perform decryption
    public static BigInteger decrypt(BigInteger encrypted, BigInteger d, BigInteger n) {
        return pow(encrypted, d, n);
    }

 }
