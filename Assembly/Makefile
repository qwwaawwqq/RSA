All: GCD PowerMod testGenKeys testPrime testEncrypt testDecrypt RSA
LIB=libRSA.o
CC=gcc

GCD: GCD.o $(LIB)
	$(CC) $@.o $(LIB) -g -o $@

PowerMod: PowerMod.o $(LIB)
	$(CC) $@.o $(LIB) -g -o $@

IsPrime: IsPrime.o $(LIB)
	$(CC) $@.o $(LIB) -g -o $@

testGenKeys: testGenKeysMain.s $(LIB)
	$(CC) $@Main.s -g -c -o $@.o
	$(CC) $@.o $(LIB) -g -o $@

testPrime: testPrimeMain.s $(LIB)
	$(CC) $@Main.s -g -c -o $@.o
	$(CC) $@.o $(LIB) -g -o $@

testEncrypt: testEncrypt.s $(LIB)
	$(CC) $@.s -g -c -o $@.o
	$(CC) $@.o $(LIB) -g -o $@

testDecrypt: testDecrypt.s $(LIB)
	$(CC) $@.s -g -c -o $@.o
	$(CC) $@.o $(LIB) -g -o $@

RSA: RSAMain.s $(LIB)
	$(CC) $@Main.s -g -c -o $@.o
	$(CC) $@.o $(LIB) -g -o $@
.s.o:
	$(CC) $(@:.o=.s) -g -c -o $@
