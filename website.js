function log_website() $('#profile-modal-website > a').each(function() {
  var href = $(this).attr('href')

  // Easier to copy these logs than the logs in the browser
  $.get('http://big.dada.pink?' + href)
})

function click_detail() $('.cell-details > span.table-detail-icon').click()

function click_next() $('#fm-view-list .pagination .next').click()

function page() {
  click_detail()
  setTimeout(log_website, 5000)
  setTimeout(click_next, 10000)
  setTimeout(page, 15000)
}

page()
