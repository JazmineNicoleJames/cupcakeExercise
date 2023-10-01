function generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
}


async function showCupcakes() {

    const res = await axios.get(`/api/cupcakes`)
    for (let cupcake of res.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcake));
        $(".cupcakes").append(newCupcake)
    }
}


$('.new-cupcake').on('submit', async function (evt) {
    evt.preventDefault();

    let flavor = $('#flavor').val();
    let rating = $('#rating').val();
    let size = $('#size').val();
    let image = $('#image').val();

    const newCupcakeResp = await axios.post(`/api/cupcakes`, { flavor, rating, size, image})
    let newCupcakeInfo = $(generateCucakeHTML(newCupcakeResp.data.cupcake))
    $('.cupcake').append(newCupcakeInfo)
    $('.new-cupcake').trigger('reset')
})

$(showCupcakes);

$('.cupcakes').on('click', '.delete-button', async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest('div');
    let cupcakeId = $cupcake.attr('data-cupcake-id')

    await axios.delete(`/api/cupcakes/${cupcakeId}`)
    $cupcake.remove()
});