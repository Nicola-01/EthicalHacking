TARGET = retlib

all: ${TARGET}

N = 12
retlib: retlib.c
	gcc -m32 -DBUF_SIZE=${N} -fno-stack-protector -z noexecstack -o $@ $@.c
	sudo chown root $@ && sudo chmod 4755 $@
	mv retlib retlib1

clean:
	rm -f *.o *.out ${TARGET} badfile
