$(function(){
    $(".a_photo").click(function(){
        create_table();

        $('#modal_thumbnail').modal('show');
    });
});

function create_table() {
    $("#modal_body_thumbnail").empty();
    $("#modal_body_thumbnail").append("<h5 class='text-center'>Hello. Some text here.</h5>");
    $("#modal_body_thumbnail").append(get_table_body(1000));
    $("#modal_body_thumbnail").append(get_table_body(1001));
    $("#modal_body_thumbnail").append(get_table_body(1002));
    $("#modal_body_thumbnail").append(get_table_body(1003));
    $("#modal_body_thumbnail").append(get_table_body(1004));
}

function get_table_body(pid) {
    var table_header =
        "<div class='table-responsive'>" +
            "<table class='table table-striped modal_thumbnail_table'>" +
                "<tbody>" +
                    "<tr>";
    var table_footer =
                    "</tr>" +
                "</tbody>" +
            "</table>" +
        "</div>";
    var table_data = get_table_data(pid)
    return table_header + table_data + table_footer;
}

function get_table_data(pid) {
    var table_data = ""
    for (var i = 0; i < 10; i++) {
        var img_url = '"/static/photos/' + pid + '.jpg"'
        table_data +=
            "<td class='modal_thumbnail_row'>" +
                "<div class='thumbnail' style='background-image: url(" + img_url + ")'></div>" +
            "</td>";
    }
    return table_data;
}
