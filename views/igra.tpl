%import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <h2>{{igra.pravilni_del_gesla()}}</h2>
  <h2>{{Napačnih ugibov: {igra.nepravilni_ugibi()}}</h2>

  % if poskus == 'Z':
  <h1> zmagala si </h1>
  % elif poskus == 'X':
  <h1> izgubil si </h1>
  %else:

  <img src="img/10.jpg" alt="obesanje">

  <form action="/igra/{{id_igra}}/" method="post">
  Črka: <unput type='text' name='crka'>
    <button type="submit">Ugibaj novo črko</button>
  </form>
  % end
</body>

</html>