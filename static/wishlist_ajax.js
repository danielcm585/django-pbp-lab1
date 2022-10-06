const table = document.getElementById('table')

$(document).ready(() => {
  $.get('/wishlist/json', (wishlists) => {
    wishlists.forEach((wishlist) => {
      $('#table').append(`
        <tr class="item-table-row">
          <th class="item-table-cell">${wishlist.fields.nama_barang}</th>
          <th class="item-table-cell">${wishlist.fields.harga_barang}</th>
          <th class="item-table-cell">${wishlist.fields.deskripsi}</th>
        </tr>
      `)
    })
  })
  
  $('#form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/wishlist/ajax/submit',
      type: 'POST',
      dataType: 'json',
      data: $('#form').serialize(),
      success: (resp) => {
        console.log(resp)
        $('#table').append(`
          <tr class="item-table-row">
            <th class="item-table-cell">${resp.nama_barang}</th>
            <th class="item-table-cell">${resp.harga_barang}</th>
            <th class="item-table-cell">${resp.deskripsi}</th>
          </tr>
        `)
      },
      error: () => {
        alert("ERROR")
      }
    })
  })
})