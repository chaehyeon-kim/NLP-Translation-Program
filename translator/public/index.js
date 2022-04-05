$(document).ready(function () {
  function translate() {
    const text = $('#source').val();
    const $target = $('#target');

    $.ajax({
      url: 'translator',
      type: 'POST',
      data: { text }
    }).then(function (result) {
      $(target).val(result.text);
    });
  }

  function addTranslator() {
    const english = $('#add-english').val();
    const korean = $('#add-korean').val();

    if (english === '' || korean === '') {
      alert('English와 Korean 모두 입력해주세요.');
      return;
    }

    $.ajax({
      url: 'translator/add',
      type: 'POST',
      data: {
        english: english,
        korean: korean
      }
    }).then(function (result) {
      const status = result.text;

      if (status !== 'success') {
        alert('error');
        return;
      }

      $('#add-english').val('');
      $('#add-korean').val('');
    });
  }

  $('#translator').click(translate);
  $('#submit-btn').click(addTranslator);
});