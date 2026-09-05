program quad_gl            ! loest ax^2+bx+c=0
  implicit none
  logical, parameter :: TEST = .false.
  integer, parameter :: RP = selected_real_kind(6)
  real(kind=RP) :: a, b, c, x1, x2, d, w, e

  write (unit=*, fmt=*) "Bitte a, b, c eingeben!"
  read (unit=*, fmt=*) a, b, c

  ! tiny(a): kleinste @\underline{\textcolor{FHorange}{normalisierte}}@ Zahl > 0,
  ! die wie a aussieht
  e = max(abs(a), abs(b), abs(c), tiny(a))
  a = a/e
  b = b/e
  c = c/e
  e = a + a
  t: if ( a==0 ) then           ! linear, bx + c = 0
     if ( b/=0 ) then
        write (unit=*, fmt=*) "EINE Loesung =", -c/b
     else if ( c==0 ) then
        write (unit=*, fmt=*) "Jedes x ist Loesung"
     else
        write (unit=*, fmt=*) "Keine Loesung"
     end if
  else t                        ! quadratisch
     d = b*b - (e + e)*c; w = sqrt(abs(d))
     u: if ( d >= 0 ) then       ! reelle Loesungen
        x1 = -(b + sign(w, b))/e ! |x1|>=|x2|
        if ( x1/=0 ) then; x2 = (c/a)/x1
        else; x2 = 0
        end if                  ! kein -,
                                ! kein Stellenverlust
        write (unit=*, fmt=*) "2 Loesungen:", x1, x2
        ! naechster if-Block wegoptimiert, TEST: .false.
        if ( TEST ) then
           write (unit=*, fmt=*) (-b + sign(w, b))/e
        end if
     else                       ! komplexe Loesungen
        write (unit=*, fmt=*) -b/e, "+-i*", w/e
     end if u                   ! u nicht F
  end if t                      ! t nicht F
end program quad_gl
