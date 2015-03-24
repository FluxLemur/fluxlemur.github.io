/** Create Code Mirror editor **/

var editor = CodeMirror.fromTextArea(document.getElementById("input"), {
  lineNumbers: true,
  styleActiveLine: true,
  mode: "python",
  indentUnit: 4,
  theme: "monokai",
  viewportMargin: Infinity,
});
editor.on("change", function() {editor.getTextArea().innerHTML = editor.getValue()});

// changes tabs to spaces
n_space = 4
editor.setOption("extraKeys", {
  Tab: function(cm) {
    var spaces = Array(cm.getOption('indentUnit')+1).join(" ");
    cm.replaceSelection(spaces);
  },
  'Ctrl-Space': function() {
    runit('input', 'output');
}});

function setSource() {
  var select = document.getElementById("select");
  if (!select)
    return;
  var program = select.options[select.selectedIndex].innerHTML;
  $.get('/assets/python/'+program.toLowerCase()+'.py').done(function(source) {
    editor.setValue(source);
    document.getElementById("output").innerHTML = '';
  });
}

setSource();
setExplanation();
