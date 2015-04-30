function log_website() $('#profile-modal-website > a').each(function() {
  var href = $(this).attr('href')

  // Easier to copy these server logs than the logs in the browser
  document.body.innerHTML += '<img src="http://dada.pink/?foundation_maps&href=' + href + '" />'

})

function click_detail() $('.cell-details > span.table-detail-icon').click()
function click_close_modal() $('button.close').click()
function click_next() $('#fm-view-list .pagination .next').click()

function page() {
  click_detail()
  setTimeout(log_website, 5000)
  setTimeout(click_close_modal, 9000)
  setTimeout(click_next, 10000)
  setTimeout(page, 15000)
}

page()
