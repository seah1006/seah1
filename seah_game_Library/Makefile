CC = gcc
CFLAGS = -O2 -Wall -Wextra -std=c11
AR = ar
ARFLAGS = rcs

LIB = libseah_game.a       
OBJS = seah_game.o         
EXE = seah_demo            


all: $(LIB) $(EXE)


$(LIB): $(OBJS)
	$(AR) $(ARFLAGS) $@ $^


seah_game.o: seah_game.c seah_game.h
	$(CC) $(CFLAGS) -c seah_game.c -o seah_game.o


$(EXE): main.c $(LIB)
	$(CC) $(CFLAGS) main.c -L. -lseah_game -o $(EXE)


clean:
	rm -f $(OBJS) $(LIB) $(EXE)
