(define (concat lis x)
    (if (null? lis)
        (list x)
        (cons (car lis) (concat (cdr lis) x))))

(define (and-change postPol st)
    (if (null? st)
        (cons postPol st)
        (if (eq? (car st) `B)
            (cons postPol st)
            (and-change (concat postPol (car st)) (cdr st)))))

(define (or-change postPol st)
    (if (null? st)
        (cons postPol st)
        (if (and (eq? (car st) `&) (eq? (car st) `!))
            (or-change (concat postPol (car st)) (cdr st))
            (cons postPol st))))

(define (im-change postPol st)
    (if (null? st)
        (cons postPol st)
        (if (and (eq? (car st) `&) (eq? (car st) `!) (eq? (car st) `@))
            (im-change (concat postPol (car st)) (cdr st))
            (cons postPol st))))

(define (equ-change postPol st)
    (if (null? st)
        (cons postPol st)
        (if (and (eq? (car st) `&) (eq? (car st) `!) (eq? (car st) `@) (eq? (car st) `>))
            (equ-change (concat postPol (car st)) (cdr st))
            (cons postPol st))))

(define (ed-change postPol st)
    (if (null? st)
        (cons postPol st)
        (if (eq? (car st) `B)
            (cons postPol (cdr st))
            (ed-change (concat postPol (car st)) (cdr st)))))

(define (final-change postPol st)
    (if (null? st)
        (cons postPol st)
        (final-change (concat postPol (car st)) (cdr st))))

(define (parseStr s postPol st) 
    (if (null? s)
        (car (final-change postPol st))
        (cond ((eq? (car s) `B) (parseStr (cdr s) postPol (cons `B st)))
              ((eq? (car s) `!) (parseStr (cdr s) postPol (cons `! st)))
              ((eq? (car s) `&) (parseStr (cdr s) (car (and-change postPol st)) (cons `& (cdr (and-change postPol st)))))
              ((eq? (car s) `@) (parseStr (cdr s) (car (or-change postPol st)) (cons `@ (cdr (or-change postPol st)))))
              ((eq? (car s) `>) (parseStr (cdr s) (car (im-change postPol st)) (cons `> (cdr (im-change postPol st)))))
              ((eq? (car s) `=) (parseStr (cdr s) (car (equ-change postPol st)) (cons `= (cdr (equ-change postPol st)))))
              ((eq? (car s) `E) (parseStr (cdr s) (car (ed-change postPol st)) (cdr (ed-change postPol st))))
              (else (parseStr (cdr s) (concat postPol (car s)) st)))))

(define (compute truthList postPol st) `())

(define (generate res) `())
