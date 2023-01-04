
function button_callback() {
  var xhrReq = new XMLHttpRequest();
  xhrReq.withCredentials = true;
  var formData = new FormData;

  var text_send = document.getElementById('send');
  var text_recv = document.getElementById('reply');
  formData.append('send', text_send.value);
  //formData.append('recv', '456');
  xhrReq.onreadystatechange = function () {
    if (xhrReq.readyState == xhrReq.DONE) {
      if (xhrReq.status === 200) {
        //console.log(xhrReq.responseText);
        text_recv.value = xhrReq.responseText;
      }
    }
  }
  xhrReq.open('POST', 'http://127.0.0.1:1000/test');
  xhrReq.send(formData);
  text_send.value = "";
  text_recv.value = "正在发送问题到OpenAI,等待..."
}
