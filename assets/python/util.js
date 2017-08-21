/** Utility functions for running python script using page elements **/

function builtinRead(x) {
  // reads built-in python modules
  // note that many are not implemented in Skulpt
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

function runit(in_id, out_id) {
  // runs python interpreter on the value in in_id element
  // and outputs the results in out_id element
  var input = document.getElementById(in_id).value;
  var output = document.getElementById(out_id);
  output.innerText = '';
  Sk.pre = out_id;
  Sk.configure({output:function(text) {
    output.innerHTML = output.innerHTML + text;
  }, read:builtinRead});
  try {
    eval(Sk.importMainWithBody("<stdin>",false,input));
  }
  catch(e) {
    output.innerHTML = e.toString()
  }
}
