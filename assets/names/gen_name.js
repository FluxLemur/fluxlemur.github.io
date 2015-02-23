function rand_elem(list) {
  return list[Math.floor(Math.random()*list.length)]
}

function rand_mix(lista, listb) {
  return rand_elem(lista) + rand_elem(listb)
}

function gen_name() {
  $.get('/assets/names/animals.txt').done(function(anims) {
    $.get('/assets/names/math_terms.txt').done(function(maths) {
      animals = anims.split('\n')
      math_terms = maths.split('\n')
      math_animal = rand_mix(math_terms, animals)

      display = document.getElementById("display_name");
      display.textContent = math_animal
    })
  })
};
