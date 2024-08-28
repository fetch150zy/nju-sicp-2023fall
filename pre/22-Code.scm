(define (nats start) 
	(cons-stream start (nats (+ start 1))))

(define (add-stream s1 s2)
	(cons-stream (+ (car s1) (car s2))
		(add-stream (cdr-stream s1) (cdr-stream s2))))

(define ones (cons-stream 1 ones))

(define ints (cons-stream 1 (add-stream ones ints)))

(define (map-stream fn s)
	(if (null? s)
		nil
		(cons (fn (car s))
			(map-stream fn (cdr-stream s)))))

(define (stream-to-list s num-elements)
	(if (or (null? s) (= 0 num-elements))
		nil
		(cons (car s) (stream-to-list (cdr-stream s) (- num-elements 1)))))


