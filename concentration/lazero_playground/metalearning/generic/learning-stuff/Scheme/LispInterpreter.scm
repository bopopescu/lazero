; This is a Lisp Interpreter.
; Some code comes from <SICP>.
; Author : Brethland, Late 2019.

(define apply-in-underlying-scheme apply)
(define (eval exp env)
    (cond ((self-evaluating? exp) exp)
          ((variable? exp) (lookup-variable-value exp env))
          ((quoted? exp) (text-of-quotation exp))
          ((assignment? exp) (eval-assignment exp env))
          ((definition? exp) (eval-definition exp env))
          ((lambda? exp) (make-procedure (lambda-parameters exp)
                                         (lambda-body exp)
                                         env))
          ((begin? exp) (eval-sequence (begin-actions exp) env))
          ((cond? exp) (eval (cond->if exp) env))
          ((application? exp) (apply (eval (operator exp) env) (list-of-values (oprands exp) env)))
          (else (error "Unknown expression type -- EVAL" exp))))
(define (apply procedure arguments)
    (cond ((primitive-procedure? procedure)
            (apply-primitive-procedure procedure arguments))
          ((compound-procedure? procedure)
            (eval-sequence
                (procedure-body procedure)
                (extend-environment (procedure-parameters procedure) arguments (procedure-environment procedure))))
          (else (error "Unknown procedure type -- APPLY" procedure))))
(define (list-of-values exps env)
    (if (no-oprands? exps)
        `()
        (cons (eval (first-oprand exps) env)
              (list-of-values (rest-oprands exps) env))))
(define (eval-if exp env)
    (if (true? (eval (if-predicate exp) env))
        (eval (if-consequent exp) env)
        (eval (if-alternative exp) env)))
(define (eval-unless exp env)
    (if (false? (eval (if-predicate exp) env))
        (eval (if-consequent exp) env)
        (eval (if-alternative exp) env)))
(define (eval-sequence exps env)
    (cond ((last-exp? exps) (eval (first-exp exps) env))
        (else (eval (first-exp exps) env)
              (eval-sequence (rest-exps exps) env))))
(define (eval-assignment exp env)
    (set-variable-value! (assignment-variable exp)
                         (eval (assignment-value exp) env)
                         env)
    `ok)
(define (eval-definition exp env)
    (define-variable! (definition-variable exp)
                      (eval (definition-value exp) env)
                      env)
    `ok)
(define (self-evaluating? exp)
    (cond ((number? exp) #t)
          ((string? exp) #t)
          (else #f)))
(define (variable? exp) (symbol? exp))
(define (quoted? exp)
    (tagged-list? exp `quote))
(define (text-of-quotation exp) (car (cdr exp)))
(define (tagged-list? exp tag)
    (if (pair? exp)
        (eq? (car exp) tag)
        #f))
(define (assignment? exp)
    (tagged-list? exp `set!))
(define (assignment-variable exp) (car (cdr exp)))
(define (assignment-value exp) (car (cdr (cdr exp))))
(define (definition? exp)
    (tagged-list? exp `define))
(define (definition-variable exp)
    (if (symbol? (car (cdr exp)))
        (car (cdr exp))
        (car (car (cdr exp)))))
(define (definition-value exp)
    (if (symbol? (car (cdr exp)))
        (car (cdr (cdr exp)))
        (make-lambda (cdr (car (cdr exp)))
                     (cdr (cdr exp)))))
(define (lambda? exp) (tagged-list? exp `lambda))
(define (lambda-parameters exp) (car (cdr exp)))
(define (lambda-body exp) (cdr (cdr exp)))
(define (make-lambda parameters body)
    (cons `lambda (cons parameters body)))
(define (if? exp) (tagged-list? exp `if))
(define (if-predicate exp) (car (cdr exp)))
(define (if-consequent exp) (car (cdr (cdr exp))))
(define (if-alternative exp)
    (if (not (null? (cdr (cdr (cdr exp)))))
        (car (cdr (cdr (cdr exp))))
        #f))
(define (make-if predicate consequent alternative)
    (list `if predicate consequent alternative))
(define (begin? exp) (tagged-list? exp `begin))
(define (begin-actions exp) (cdr exp))
(define (last-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))
(define (sequence->exp seq)
    (cond ((null? seq) seq)
          ((last-exp? seq) (first-exp seq))
          (else (make-begin seq))))
(define (make-begin seq) (cons `begin seq))
(define (application? exp) (pair? exp))
(define (operator exp) (car exp))
(define (oprands exp) (cdr exp))
(define (no-oprands? ops) (null? ops))
(define (first-oprand ops) (car ops))
(define (rest-oprands ops) (cdr ops))
(define (cond? exp) (tagged-list? exp `cond))
(define (cond-clauses exp) (cdr exp))
(define (cond-else-clause? clause)
    (eq? (cond-predicate clause) `else))
(define (cond-predicate clause) (car clause))
(define (cond-actions clause) (cdr clause))
(define (cond->if exp)
    (expand-clauses (cond-clauses exp)))
(define (expand-clauses clauses)
    (if (null? clauses)
        `false
        (let ((first (car clauses))
              (rest (cdr clauses)))
            (if (cond-else-clause? first)
                (if (null? rest)
                    (sequence->exp (cond-actions first))
                    (error "ELSE clause isn't last -- COND->IF" clauses))
                (make-if (cond-predicate first)
                         (sequence->exp (cond-actions first))
                         (expand-clauses rest))))))
(define (or? exp) (tagged-list? exp `or))
(define (and? exp) (tagged-list? exp `and))
(define (or-body exp) (cdr exp))
(define (and-body exp) (cdr exp))
(define (first-predicate exp) (car exp))
(define (rest-predicate exp) (car exp))
(define (eval-or clauses env)
    (if (null? clauses)
        #f
        (if (true? (eval (first-predicate clauses) env))
            #t
            (eval-or (rest-predicate clauses) env))))
(define (eval-and clauses env)
    (if (null? clauses)
        #t
        (if (false? (eval (first-predicate clauses) env))
            #f
            (eval-and (rest-predicate clauses) env))))
(define (cond-form-predicate clause) (car clause))
(define (cond-form-process clause) (car (cdr (cdr clause))))
(define (cond-form stream env)
    (if (null? (cdr stream))
        (if (eq? `else (cond-form-predicate (car stream)))
            (car (cdr (car stream)))
            #f)
        (let ((first (car stream))
              (second (cdr stream)))
            (let ((eval-value (eval (cond-form-predicate first) env)))
            (cond ((eq? eval-value `else) (error "ERROR ELSE isn't an end. --COND-FORM" first))
                  ((true? eval-value) ((cond-form-process first) eval-value))
                  (else (cond-form second env)))))))
(define (let-variable-list exp) (car (cdr exp)))
(define (get-variable-list exp)
    (if (null? exp)
        `()
        (cons (car (car exp))
            (get-variable-list (cdr exp)))))
(define (get-arguments-list exp)
    (if (null? exp)
        `()
        (cons (cdr (car exp))
            (get-arguments-list (cdr exp)))))
(define (let->combination exp)
    (append (make-lambda (get-variable-list (let-variable-list exp))
                        (car (cdr (cdr exp))))
            (get-arguments-list (let-variable-list exp))))
; (define (make-let variable-list)
;     (list `let variable-list))
; (define (let*->nested-lets exp)
;     (let ((variable-list) (get-variable-list exp))
;         (define (iter result exp)
;         (cond ((null? (cdr exp)) (cons result (make-let (car exp))))
;               (else (iter (cons result (make-let (car exp)))
;                             (cdr exp)))))
;         (iter `() variable-list)))
; (define (for? exp) (tagged-list? exp `for))
; (define (for-to-lambda exp)
;     (let ((predicate (cadr exp))
;           (iter-function (caddr exp))
;           (function (cadddr exp))
;           (init-value (caddddr exp)))
;     `((define (lamdba-func it)
;         (cond (((not (predicate it)) `())
;                   (else (begin function (lambda-func (iter-function it)))))))
;       (lambda-func init-value))))
(define (true? x)
    (not (eq? x #f)))
(define (false? x)
    (eq? x #f))
(define (make-procedure parameters body env)
    (list `procedure parameters body env))
(define (compound-procedure? p)
    (tagged-list? p `procedure))
(define (procedure-parameters p) (car (cdr p)))
(define (procedure-body p) (car (cdr (cdr p))))
(define (procedure-environment p) (car (cdr (cdr (cdr p)))))
(define (enclosing-environment env) (cdr env))
(define (first-frame env) (car env))
(define the-empty-environment `())
(define (make-frame variables values)
    (cons variables values))
; (define (make-frame variables values)
;     (if (null? variables)
;         `()
;         (cons (cons (car variables) (car values))
;             (make-frame (cdr variables) (cdr values)))))
(define (frame-variables frame) (car frame))
(define (frame-values frame) (cdr frame))
(define (add-binding-to-frame! var val frame)
    (set-car! frame (cons var (car frame)))
    (set-cdr! frame (cons val (cdr frame))))
; (define (add-binding-to-frame! var val frame)
;     (set! frame (cons (cons var val) frame)))
(define (extend-environment vars vals base-env)
    (if (= (length vars) (length vals))
        (cons (make-frame vars vals) base-env)
        (if (< (length vars) (length vals))
            (error "Too many arguments supplied" vars vals)
            (error "Too few arguments supplied" vars vals))))
(define (lookup-variable-value var env)
    (define (env-loop env)
        (define (scan vars vals)
            (cond ((null? vars) (env-loop (enclosing-environment env)))
                  ((eq? var (car vars))
                    (car vals))
                  (else (scan (cdr vars) (cdr vals)))))
        (if (eq? env the-empty-environment)
            (error "Unbound variable" var)
            (let ((frame (first-frame env)))
                (scan (frame-variables frame)
                      (frame-values frame)))))
    (env-loop env))
(define (set-variable-value! var val env)
    (define (env-loop env)
        (define (scan vars vals)
            (cond ((null? vars) (env-loop (enclosing-environment env)))
                  ((eq? var (car vars))
                    (set-car! vals val))
                  (else (scan (cdr vars) (cdr vals)))))
        (if (eq? env the-empty-environment)
            (error "Unbound variable -- SET!" var)
            (let ((frame (first-frame env)))
                (scan (frame-variables frame)
                      (frame-values frame)))))
    (env-loop env))
(define (define-variable! var val env)
    (let ((frame (first-frame env)))
        (define (scan vars vals)
            (cond ((null? vars) (add-binding-to-frame! var val frame))
                  ((eq? var (car vars)) (set-car! vals val))
                  (else (scan (cdr vars) (cdr vals)))))
        (scan (frame-variables frame)
              (frame-values frame))))
; (define (make-unbound var env)
;     (let ((frame (first-frame env)))
;         (define (scan vars vals)
;             (cond ((null? vars 
;                     (display "No such variables in scope" var)))
;                   ((eq? var (car vars)) (set-cdr! vals (cdr vals)) (set-cdr! vars (cdr vars)))
;                   (else scan (cdr vars) (cdr vals))))
;         (scan (frame-variables frame)
;               (frame-values frame))))
(define primitive-procedures
    (list (list `car car)
          (list `cdr cdr)
          (list `cons cons)
          (list `null? null?)
          (list `eq? eq?)
          (list `+ +)
          (list `* *)
          (list `- -)
        ;   (list `set! set!)
          (list `/ /)))
(define (primitive-procedure-names)
    (map car primitive-procedures))
(define (primitive-procedure-objects)
    (map (lambda (proc) (list `primitive (car (cdr proc)))) primitive-procedures))
(define (setup-environment)
    (let ((initial-env  (extend-environment (primitive-procedure-names)
                                            (primitive-procedure-objects)
                                            the-empty-environment)))
        (define-variable! `true #t initial-env)
        (define-variable! `false #f initial-env)
        initial-env))
(define the-global-environment (setup-environment))
(define (primitive-procedure? proc)
    (tagged-list? proc `primitive))
(define (primitive-implementation proc) (car (cdr proc)))
(define (apply-primitive-procedure proc args)
    (apply-in-underlying-scheme
        (primitive-implementation proc) args))
(define input-prompt ";;; M-Eval input:")
(define output-prompt ";;; M-Eval output:")
(define (driver-loop)
    (prompt-for-input input-prompt)
    (let ((input (read)))
        (let ((output (eval input the-global-environment)))
            (announce-output output-prompt)
            (user-print output)))
    (driver-loop))
(define (prompt-for-input string)
    (newline)
    (newline)
    (display string)
    (newline))
(define (announce-output string)
    (newline)
    (display string)
    (newline))
(define (user-print object)
    (if (compound-procedure? object)
        (display (list `compound-procedure
                        (procedure-parameters object)
                        (procedure-body object)
                        `<procedure-env>))
        (display object)))
(driver-loop)
; ((lambda (n)
;     ((lambda (fib)
;         (fib fib n))
;         (lambda (body k)
;             (cond ((= k 0) 0)
;                   ((= k 1) 1)
;                   (else (+ (body body (- k 1))
;                             (body body (- k 2)))))))) 5)
;  (define Y-combinator 
;    (lambda (f) 
;      ((lambda (x) (x x)) 
;       (lambda (x) (f (lambda (y) ((x x) y))))))) 
; (define fib
;     (lambda (f)
;         (lambda (n)
;             (cond ((= n 0) 0)
;                   ((= n 1) 1)
;                   (else (+ (f (- n 1)) (f (- n 2))))))))
; (define (f x)
;     ((lambda (even? odd?)
;         (even? even? odd? x))
;         (lambda (ev? od? n)
;             (if (= n 0) true (od? ev? od? (- n 1))))
;             (lambda (ev? od? n)
;                 (if (= n 0) false (ev? ev? od? (- n 1))))))
; (f 10)
; (f 5)
; ((Y-combinator fib) 10)