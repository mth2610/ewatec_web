$(document).ready(function () {
    // using jQuery

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    $(document).click(function (e) {
        var $that = $(e.target);
        // -----------------------------------------Extract data-----------------------------------------

        if ($that.closest("#extract_data")[0]) {
            $("#spinner").show();
            var id = document.getElementById("id").value;
            var varibale = document.getElementById("variable").value;
            var start_time = document.getElementById("starttime").value;
            var end_time = document.getElementById("endtime").value;
            var timstep = ($that.closest("#extract_data")[0]).getAttribute("timestep");
             
            $.ajax({
                async:true,
                type: 'POST',
                url: 'extract_data',
                data: {
                    'id':document.getElementById("id").value ,
                    'variable': ($that.closest("#extract_data")[0]).getAttribute("variable"),
                    'starttime': ($that.closest("#extract_data")[0]).getAttribute("starttime"),
                    'endtime': ($that.closest("#extract_data")[0]).getAttribute("endtime"),
                    'timestep': ($that.closest("#extract_data")[0]).getAttribute("timestep")
                },
                complete: function() {
                $("#spinner").hide();
                },  
                success: function (url) {
                    window.location = url;
                },
                error: function () {
                    alert('Failed in sending ajax request')
                },
                dataType: 'html',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            });
        };
        // -----------------------------------------Monthly Graph-----------------------------------------
        if ($that.closest("#monthly_statistic")[0] || $that.closest("#yearly_statistic")[0] || $that.closest("#daily_statistic")[0] || $that.closest("#hourly_statistic")[0]|| $that.closest("#initial_statistic")[0]) {      
            $("#spinner").show();
            var id = String(document.getElementById("id").value);
            var varibale = String(document.getElementById("variable").value);
            var start_time = String(document.getElementById("starttime").value);
            var end_time = String(document.getElementById("endtime").value);
            var id_container;
            
            if(document.getElementById('removeoutlier').checked == true){
                var removeoutlier = "True";
            }else{
                var removeoutlier = "False";
            };
            
            
            if(document.getElementById('filldata').checked == true){
                var filldata = "True";
            }else{
                var filldata = "False";
            };
            
            if(document.getElementById('linear_regression').checked == true){
                var linear_regression = "True";
            }else{
                var linear_regression = "False";
            };
            
            if ($that.closest("#yearly_statistic")[0]) {
                var timestep = "AS";
                id_container = "yearly_content";
            } else if ($that.closest("#monthly_statistic")[0]) {
                var timestep = "M";
                id_container = "monthly_content";
            } else if ($that.closest("#daily_statistic")[0]) {
                var timestep = "D";
                id_container = "daily_content";
            } else if ($that.closest("#hourly_statistic")[0]) {
                var timestep = "H";
                id_container = "hourly_content";
            }else if ($that.closest("#initial_statistic")[0]) {
                var timestep = "raw";
                id_container = "initial_data_content";
            };

            $.ajax({
                async:true,
                type: 'POST',
                url: 'resample_data',
                data: {
                    'id': String(document.getElementById("id").value),
                    'variable': String(document.getElementById("variable").value),
                    'starttime': String(document.getElementById("starttime").value),
                    'endtime': String(document.getElementById("endtime").value),
                    'timestep': timestep,
                    'removeoutlier':removeoutlier,
                    'filldata':filldata,
                    'linear_regression':linear_regression,
                },
                complete: function() {
                $("#spinner").hide();
                },  
                success: function (data) {
                    $(document.getElementById(id_container)).append(data)

                },
                error: function () {
                    alert('Failed in sending ajax request')
                },
                dataType: 'html',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            });


        } else if ($that.closest("#histogram_statistic")[0]) {
            $("#spinner").show();
            var id = String(document.getElementById("id").value);
            var varibale = String(document.getElementById("variable").value);
            var start_time = String(document.getElementById("starttime").value);
            var end_time = String(document.getElementById("endtime").value);
            var id_container = "histogram_content";
            
            if(document.getElementById('removeoutlier').checked == true){
                var removeoutlier = "True";
            }else{
                var removeoutlier = "False";
            };
            
            if(document.getElementById('filldata').checked == true){
                var filldata = "True";
            }else{
                var filldata = "False";
            };
            
            if(document.getElementById('linear_regression').checked == true){
                var linear_regression = "True";
            }else{
                var linear_regression = "False";
            };
            
            $.ajax({
                async:true,
                type: 'POST',
                url: 'histogram_statistics',
                data: {
                    'id': String(document.getElementById("id").value),
                    'variable': String(document.getElementById("variable").value),
                    'starttime': String(document.getElementById("starttime").value),
                    'endtime': String(document.getElementById("endtime").value),
                    'removeoutlier':removeoutlier,
                    'filldata':filldata,
                    'linear_regression':linear_regression,
                },
                complete: function() {
                $("#spinner").hide();
                },  
                success: function (data) {
                    $(document.getElementById(id_container)).append(data)
                },
                error: function () {
                    alert('Failed in sending ajax request')
                },
                dataType: 'html',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            });
        } else if ($that.closest("#averagemonthly_statistic")[0]) {
            $("#spinner").show();
            var id = String(document.getElementById("id").value);
            var varibale = String(document.getElementById("variable").value);
            var start_time = String(document.getElementById("starttime").value);
            var end_time = String(document.getElementById("endtime").value);
            var id_container = "avgmonthly_content";
            
            if(document.getElementById('removeoutlier').checked == true){
                var removeoutlier = "True";
            }else{
                var removeoutlier = "False";
            };
            
            if(document.getElementById('filldata').checked == true){
                var filldata = "True";
            }else{
                var filldata = "False";
            };
            
            if(document.getElementById('linear_regression').checked == true){
                var linear_regression = "True";
            }else{
                var linear_regression = "False";
            };

            $.ajax({
                async:true,
                type: 'POST',
                url: 'averagemonthly_statistics',
                data: {
                    'id': String(document.getElementById("id").value),
                    'variable': String(document.getElementById("variable").value),
                    'starttime': String(document.getElementById("starttime").value),
                    'endtime': String(document.getElementById("endtime").value),
                    'removeoutlier':removeoutlier,
                    'filldata':filldata,
                    'linear_regression':linear_regression,
                },
                complete: function() {
                $("#spinner").hide();
                },  
                success: function (data) {
                    $(document.getElementById(id_container)).append(data)
                },
                error: function () {
                    alert('Failed in sending ajax request')
                },
                dataType: 'html',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            });
        };
    });


});