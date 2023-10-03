
// the good ones
FCT gcd[a,b]:
    <<
    WHILE[a !=! b]:
    <<
        IF << a>b >> : a=a-b  
        ELSE: b = b-a
    >>

    SENDBACK a

    >>


FCT getMax [a()]:
    <<
        max = MIN_INT
        GO_THROUGH[a->el] :
            <<
              IF << el>max >> : max=el  
            >>

    SENDBACK max
    >>

FCT print [a()]:
     <<
        GO_THROUGH[a->el] :
            <<
              el.SHOW(terminal) + ' '.SHOW(terminal)
            >>
    >>


/// the error
FCT getMin [a()]:
    <<
        max = MAX_INT
        GO_THRGH[a->el] :
            <<
              IF << el<max >> : max=el  
            >>

    SENDBACK max
    >>


FCT start[]:
    <<

    DO: gcd[2,3]

    DO: getMax[(2,4,5,6,)]

    DO: print[(2,4,5,6,)]

    DO: getMin[(2,4,5,6,)]

    >>

DO: start[]