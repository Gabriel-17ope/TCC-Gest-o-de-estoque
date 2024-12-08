document.querySelector(".btn").addEventListener("click", function (e) {
    e.preventDefault();

    const dataInicio = document.getElementById("data-inicio").value;
    const dataFim = document.getElementById("data-fim").value;
    const tipoRelatorio = document.getElementById("tipo-relatorio").value;

    const url = `/relatorio/download?data_inicio=${dataInicio}&data_fim=${dataFim}&tipo_relatorio=${tipoRelatorio}`;

    window.location.href = url;
});
