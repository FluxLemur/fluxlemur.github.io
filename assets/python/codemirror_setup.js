/** Create Code Mirror editor **/

var editorOptions = {
  lineNumbers: true,
  styleActiveLine: true,
  mode: "python",
  indentUnit: 4,
  theme: "monokai"
};

var editors = [];

function addEditor(name, enableKeystroke=false) {
  var inputName = 'input_' + name;
  var editor = CodeMirror.fromTextArea(document.getElementById(inputName), editorOptions);
  editor.on("change", function() {editor.getTextArea().innerHTML = editor.getValue()});

  // changes tabs to spaces and register "run" callback
  var outputName = 'output_' + name;
  editor.setOption("extraKeys", {
    Tab: function(cm) {
      var spaces = Array(cm.getOption('indentUnit') + 1).join(" ");
      cm.replaceSelection(spaces);
    }});
  if (enableKeystroke) {
    editor.setOption("extraKeys", {
      'Ctrl-Enter': function() {
        runit(inputName, outputName);
    }});
  }

  // add the source
  $.get('/assets/python/' + name + '.py').done(function(source) {
    editor.setValue(source);
    document.getElementById(outputName).innerHTML = '';
  });

  editors.push(editor);
};
