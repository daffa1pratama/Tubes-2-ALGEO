#include "listdp.h"
#include <stdio.h>
#include <stdlib.h>

/* File : listdp.h */
/* ADT List dengan Double Pointer */
/* Representasi berkait dengan address adalah pointer */
/* infotype adalah integer */

/* NIM              : 13518091                     */
/* Nama             : Fakhrurrida Clarendia Widodo */
/* Tanggal          : 29 Oktober 2019              */
/* Topik Praktikum  : List dengan Double Pointer   */
/* Deskripsi        : -                            */

/* PROTOTYPE */
/****************** TEST LIST KOSONG ******************/
boolean IsEmpty (List L)
/* Mengirim true jika list kosong. Lihat definisi di atas. */
{
    return (First(L) == Nil)&&(Last(L)==Nil);
}

/****************** PEMBUATAN LIST KOSONG ******************/
void CreateEmpty (List *L)
/* I.S. L sembarang  */
/* F.S. Terbentuk list kosong. Lihat definisi di atas. */
{
    First(*L) = Nil;
    Last(*L) = Nil;
}

/****************** Manajemen Memori ******************/
address Alokasi (infotype X)
/* Mengirimkan address hasil alokasi sebuah elemen */
/* Jika alokasi berhasil, maka address tidak nil. */
/* Misalnya: menghasilkan P, maka Info(P)=X, Next(P)=Nil, Prev(P)=Nil */
/* Jika alokasi gagal, mengirimkan Nil. */
{
    //KAMUS LOKAL
    address P;

    //ALGORITMA
    P = (address) malloc (sizeof(ElmtList));
    if (P!=Nil)
    {
        Info(P) = X;
        Next(P) = Nil;
        Prev(P) = Nil;
        return P;
    }
    else
    {
        return Nil;
    }
}

void Dealokasi (address P)
/* I.S. P terdefinisi */
/* F.S. P dikembalikan ke sistem */
/* Melakukan dealokasi/pengembalian address P */
{
    free (P);
}

/****************** PENCARIAN SEBUAH ELEMEN LIST ******************/
address Search (List L, infotype X)
/* Mencari apakah ada elemen list dengan Info(P)=X */
/* Jika ada, mengirimkan address elemen tersebut. */
/* Jika tidak ada, mengirimkan Nil */
{
    //KAMUS LOKAL
    address P;
    boolean status;

    //ALGORITMA
    P = First(L);
    status = false;

    while ((status==false)&&(P!=Nil))
    {
        if (Info(P)==X)
        {
            status = true;
        }
        else
        {
            P = Next(P);
        }
    }
    return P;
}

/****************** PRIMITIF BERDASARKAN NILAI ******************/
/*** PENAMBAHAN ELEMEN ***/
void InsVFirst (List *L, infotype X)
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen pertama dengan nilai X jika alokasi berhasil */
{
    //KAMUS LOKAL
    address P;

    //ALGORITME
    P = Alokasi(X);
    if (P!=Nil)
    {
        if (IsEmpty(*L))
        {
            First(*L) = P;
            Last(*L) = First(*L);
        }
        else
        {
            Prev(First(*L)) = P;
            Next(P) = First(*L);
            First(*L) = P;
        }
    }
}
void InsVLast (List *L, infotype X)
/* I.S. L mungkin kosong */
/* F.S. Melakukan alokasi sebuah elemen dan */
/* menambahkan elemen list di akhir: elemen terakhir yang baru */
/* bernilai X jika alokasi berhasil. Jika alokasi gagal: I.S.= F.S. */
{
    //KAMUS LOKAL
    address P;

    //ALGORITME
    P = Alokasi(X);
    if (P!=Nil)
    {
        if (IsEmpty(*L))
        {
            First(*L) = P;
            Last(*L) = First(*L);
        }
        else
        {
            Next(Last(*L)) = P;
            Prev(P) = Last(*L);
            Last(*L) = P;
        }
    }
}

/*** PENGHAPUSAN ELEMEN ***/
void DelVFirst (List *L, infotype *X)
/* I.S. List L tidak kosong  */
/* F.S. Elemen pertama list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen pertama di-dealokasi */
{
    //KAMUS LOKAL
    address P;

    //ALGORITMA
    P = First(*L);
    *X = Info(P);

    if (Next(P) != Nil)
    {
        Prev(Next(P)) = Nil;
        First(*L) = Next(P);
    }
    else
    {
        First(*L) = Nil;
        Last(*L) = Nil;
    }
    Dealokasi(P);

    *P = First(*L);
    First(*L) = Next(First(*L));
    Next(*P) = Nil;
    if (First(*L) == Nil)
    {
        Last(*L) = Nil;
    }
    else
    {
        Prev(First(*L)) = Nil;
    }
}
void DelVLast (List *L, infotype *X)
/* I.S. list tidak kosong */
/* F.S. Elemen terakhir list dihapus: nilai info disimpan pada X */
/*      dan alamat elemen terakhir di-dealokasi */
{
    //KAMUS LOKAL
    address P;

    //ALGORITMA
    P = Last(*L);
    *X = Info(P);

    if (Prev(P) != Nil)
    {
        Next(Prev(P)) = Nil;
        Last(*L) = Prev(P);
    }
    else
    {
        First(*L) = Nil;
        Last(*L) = Nil;
    }
    Dealokasi(P);
}

/****************** PRIMITIF BERDASARKAN ALAMAT ******************/
/*** PENAMBAHAN ELEMEN BERDASARKAN ALAMAT ***/
void InsertFirst (List *L, address P)
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. Menambahkan elemen ber-address P sebagai elemen pertama */
{
    Next(P) = First(*L);
    if (IsEmpty(*L))
    {
        First(*L) = P;
        Last(*L) = P;
    }
    else
    {
        Prev(First(*L)) = P;
        First(*L) = P;
    }
}
void InsertLast (List *L, address P)
/* I.S. Sembarang, P sudah dialokasi  */
/* F.S. P ditambahkan sebagai elemen terakhir yang baru */
{
    Prev(P) = Last(*L);
    if (IsEmpty(*L))
    {
        First(*L) = P;
        Last(*L) = P;
    }
    else
    {
        Next(Last(*L)) = P;
        Last(*L) = P;
    }
}
void InsertAfter (List *L, address P, address Prec)
/* I.S. Prec pastilah elemen list; P sudah dialokasi  */
/* F.S. Insert P sebagai elemen sesudah elemen beralamat Prec */
{
    if (Next(Prec) == Nil)
    {
        Last(*L) = P;
        Next(P) = Next(Prec);
        Prev(P) = Prec;
        Next(Prec) = P;
    }
    else
    {
        Prev(Next(Prec)) = P;
        Next(P) = Next(Prec);
        Prev(P) = Prec;
        Next(Prec) = P;
    }
}
void InsertBefore (List *L, address P, address Succ)
/* I.S. Succ pastilah elemen list; P sudah dialokasi  */
/* F.S. Insert P sebagai elemen sebelum elemen beralamat Succ */
{
    if (Prev(Succ) == Nil)
    {
        First(*L) = P;
        Next(P) = Succ;
        Prev(P) = Prev(Succ);
        Prev(Succ) = P;
    }
    else
    {
        Next(Prev(Succ)) = P;
        Next(P) = Succ;
        Prev(P) = Prev(Succ);
        Prev(Succ) = P;
    }
}

/*** PENGHAPUSAN SEBUAH ELEMEN ***/
void DelFirst (List *L, address *P)
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen pertama list sebelum penghapusan */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* First element yg baru adalah suksesor elemen pertama yang lama */
{
    *P = First(*L);
    First(*L) = Next(First(*L));
    Next(*P) = Nil;
    if (First(*L) == Nil)
    {
        Last(*L) = Nil;
    }
    else
    {
        Prev(First(*L)) = Nil;
    }
}
void DelLast (List *L, address *P)
/* I.S. List tidak kosong */
/* F.S. P adalah alamat elemen terakhir list sebelum penghapusan  */
/*      Elemen list berkurang satu (mungkin menjadi kosong) */
/* Last element baru adalah predesesor elemen pertama yg lama, jika ada */
{
    *P = Last(*L);
    if (First(*L) == Last(*L))
    {
        Last(*L) = Nil;
        Last(*L) = Prev(Last(*L));
        Prev(*P) = Nil;
    }
    else
    {
        Next(Prev(Last(*L))) = Nil;
        Last(*L) = Prev(Last(*L));
        Prev(*P) = Nil;
    }
}
void DelP (List *L, infotype X)
/* I.S. Sembarang */
/* F.S. Jika ada elemen list beraddress P, dengan Info(P)=X  */
/* maka P dihapus dari list dan didealokasi */
/* Jika tidak ada elemen list dengan Info(P)=X, maka list tetap */
/* List mungkin menjadi kosong karena penghapusan */
{
    //KAMUS LOKAL
    address P, Prec;

    //ALGORITMA
    P = Search(*L,X);

    if (P != Nil)
    {
        if (P == First(*L))
        {
            DelFirst(L,&P);
            P = Nil;
        }
        else
        {
            Prec = First(*L);
            while (Next(Prec) != P)
            {
                Prec = Next(Prec);
            }

            if (Next(Prec) == Last(*L))
            {
                DelLast(L,&P);
                P = Nil;
            }
            else
            {
                Next(Prec) = Next(P);
                Prev(Next(P)) = Prec;
            }
        }
    }
}
void DelAfter (List *L, address *Pdel, address Prec)
/* I.S. List tidak kosong. Prec adalah anggota list. */
/* F.S. Menghapus Next(Prec): */
/*      Pdel adalah alamat elemen list yang dihapus  */
{
    if (Next(Prec) == Last(*L))
    {
        DelLast(L,Pdel);
    }
    else
    {
        *Pdel = Next(Prec);
        Next(Prec) = Next(*Pdel);
        Prev(Next(*Pdel)) = Prec;
    }
}
void DelBefore (List *L, address *Pdel, address Succ)
/* I.S. List tidak kosong. Succ adalah anggota list. */
/* F.S. Menghapus Prev(Succ): */
/*      Pdel adalah alamat elemen list yang dihapus  */
{
    if (Prev(Succ) == First(*L))
    {
        DelFirst(L,Pdel);
    }
    else
    {
        *Pdel = Prev(Succ);
        Prev(Succ) = Prev(*Pdel);
        Next(Prev(*Pdel)) = Succ;
    }
}

/****************** PROSES SEMUA ELEMEN LIST ******************/
void PrintForward (List L)
/* I.S. List mungkin kosong */
/* F.S. Jika list tidak kosong, isi list dicetak dari elemen pertama */
/* ke elemen terakhir secara horizontal ke kanan: [e1,e2,...,en] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [1,20,30] */
/* Jika list kosong : menulis [] */
/* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */
{
    //KAMUS LOKAL
    address P;

    //ALGORITMA
    P = First(L);
    printf("[");
    if (!IsEmpty(L))
    {
        while (Next(P)!=Nil)
        {
            printf("%d,",Info(P));
            P = Next(P);
        }
        printf("%d",Info(P));
    }
    printf("]");
}
void PrintBackward (List L)
/* I.S. List mungkin kosong */
/* F.S. Jika list tidak kosong, isi list dicetak dari elemen terakhir */
/* ke elemen pertama secara horizontal ke kanan: [en,en-1,...,e2,e1] */
/* Contoh : jika ada tiga elemen bernilai 1, 20, 30 akan dicetak: [30,20,1] */
/* Jika list kosong : menulis [] */
/* Tidak ada tambahan karakter apa pun di awal, akhir, atau di tengah */
{
    //KAMUS LOKAL
    address P;

    //ALGORITMA
    P = Last(L);
    printf("[");
    if (!IsEmpty(L))
    {
        while (Prev(P)!=Nil)
        {
            printf("%d,",Info(P));
            P = Prev(P);
        }
        printf("%d",Info(P));
    }
    printf("]");
}

