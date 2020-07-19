


$("#menu_button").click(function() {
    if(window.matchMedia("(min-width: 500px)").matches)
        {
            document.getElementById("side_menu").style.width = "30%";
        }
    else
        {
            document.getElementById("side_menu").style.width = "60%";
        }
    $("#side_menu").toggle();
});


$("#user_options").click(function() {
    $("#user_options_menu").toggle();
});


$(document).ready( function() {
    if(window.matchMedia("(max-width: 576px)").matches)
    {
        $("h1.display-3").addClass("display-4");
        $("h1.display-3").removeClass("display-3");
    }
    $("button.btn").click(function() {
        console.log("clicked");
        location.href = "index.html";
    });
});


// ---- Book page insert and exe functions --------------

function addBook()
{

    var bookName = $("#Bookname").val()
    var bookImg= $("#img").attr("src");
    var bookToAdd={name:bookName, src:bookImg };
    sessionStorage.setItem("book", JSON.stringify(bookToAdd));

}

function loadBookPage(name , source , information)
{
    console.log(name);
    $(".fullscreen[name='" + name + "']").show();
    $(".book-page-image").attr("src" , source);
    $(".book_page_container > span").html("");
    $(".book_page_container > span").html(name);
    $("#read_a_sample_panel > p").html(information);
    $(".close-button-book-page").click(  function() { $(".fullscreen[name='" + name + "']").hide();} );
    //$(".flip").click(function() { $(".panel").slideToggle("slow"); });
    flip_panel_relation(name);
};

function flip_panel_relation(name) {
    $("#read_a_sample_flip[name='" + name + "']").click( function() { 
        console.log($("#read_a_sample_panel[name='" + name + "']").css('display') == 'none');
        if($("#read_a_sample_panel[name='" + name + "']").css('display') == 'none')
        {
            $("#read_a_sample_panel[name='" + name + "']").slideDown("slow"); 
        }
        else
        {
            $("#read_a_sample_panel[name='" + name + "']").slideUp("slow"); 
        }
    });
    $("#loan_now_flip[name='" + name + "']").click( function() { $("#loan_now_panel[name='" + name + "']").slideToggle("slow"); });
    $("#add_to_wishlist[name='" + name + "']").click(function(){ $(this).toggleClass("redColor");});
    $("#confirm_loan_now").click(function() {
        var d = new Date();
        $("#loan_now_panel[name='" + name + "']").empty();
        $("#loan_now_panel[name='" + name + "']").append("<div>The book will be saved for you until " + (d.getHours() + 1) + ":" + d.getMinutes() + " PM.</div>");
        $("#loan_now_panel[name='" + name + "']").append("<div class='font-weight-bold text-white' style='font-size: 2em ; text-align: center; '>53D1-000D-12CA</div><div class='text-muted text-white'>*The code will be saved to your personal page.</div>");

    });
};

function appendBookScreen(name , source, information)
{
    
    console.log(!book_page_opened.includes(name));
    if(!book_page_opened.includes(name))
    {
        var book_screen = '\n<div name="'+ name +'" class="fullscreen">\n<svg class="bi bi-x close-button-book-page" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/><path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/></svg>\n<div class="book_page_container">\n<img class="book-page-image" src="" alt="">\n<span></span>\n<div id="loan_now_flip" name="'+ name +'" class="flip">\n<i class="fas fa-book"></i><span>Loan Now</span>\n</div>\n<div id="loan_now_panel" name="'+ name +'" class="panel"><i class="fas fa-map-marker-alt"></i><span>Savidor-Center Tel Aviv</span><a href="">Change?</a><i id="confirm_loan_now" class="fas fa-check-circle"></i></div><div id="read_a_sample_flip" name="'+ name +'" class="flip"><i class="fas fa-search-plus"></i><span>Read More</span></div><div id="read_a_sample_panel" name="'+ name +'" class="panel"><p>'+ information +'</p></div><div id="add_to_wishlist" name="'+ name +'" class="flip"><i class="fas fa-heart"></i><span>Add to wishlist</span></div></div></div>';
        $("body").append(book_screen);
        book_page_opened += name;
        var d = {};
        //console.log(name , source);
    }
}

//$(document).ready(function() {
//    $("body").append(book_screen);
//  });

var book_page_opened = [];

$(document).ready(function() {

    $("img.book").click(function() {

        source = $(this).attr("src");
        name = $(this).attr("name");
        information = $(this).attr("title");
        appendBookScreen(name , source , information);
        loadBookPage(name , source , information);
    });

});

// ---------------------------------------------------------------


// Open search by clickimg on button nav search icon 

var searchScreen = '<div class="search_screen"><input class="bg-secondary" val="" type="text" id="search_input" placeholder="Name/Author/Category/ISBN"></div>';
$(document).ready(function() {
    $("body").append(searchScreen);
    $(".search_screen").hide();
});
var isSearchClicked = 0;
$("#button-nav-search").click(function() {
    if(isSearchClicked)
    {
        return;
    }
    isSearchClicked = 1;
    $(".a_footer > span").removeClass("wheatColor");
    $(".a_footer > span > i").removeClass("wheatColor");
    $("#button-nav-search > span").addClass("wheatColor");
    $("#button-nav-search > span > i").addClass("wheatColor");
    //$(".search_screen").show();
    $(".search_screen").slideDown();
    $("#search_input").slideDown();
    $(".search_screen").append("<div class='to_fit_input_search'></div>");
    var used_books = [];
    for(var i = 0; i < 20; i++)
    {
        var rand_pos_of_imgs = Math.floor(Math.random() * name_pic_relation.length);
        var book_name = name_pic_relation[rand_pos_of_imgs].name;
        if(!used_books.includes(book_name))
        {
            $(".search_screen").append('<div class="options_list_on_seacrh"></div>');
            $($(".options_list_on_seacrh")[i]).append("<img name='" + book_name + "' src='" + name_pic_relation[rand_pos_of_imgs].src + "'></img>");
            $($(".options_list_on_seacrh")[i]).append("<div class='search_list_text'><div class='font-weight-bold text-white text-left'>" + book_name + "</div><div class='font-weight-light text-white'>Author Name</div><div class='font-weight-light text-white'>Year of publication</div></div>");
            used_books += book_name;
        }
        else
        {
            i--;
        }
    }
    $(".search_screen").append("<div class='to_fit_button_nav'></div>");
    //$(".options_list_on_seacrh").append("<img name='World History' src=includes/images/bookpic.jpg></img>");

    $(".options_list_on_seacrh").click(function() {
        var source = $(this).find('img').attr('src');
        var name = $(this).find('img').attr('name');
        appendBookScreen(name , source);
        loadBookPage(name , source);
    });
    
});



// While typing search
$(document).ready(function() {
    $("#search_input").keyup( function(){ searchWhileTyping();});
});

function searchWhileTyping()
{
    var value = $("#search_input").val();
    console.log(value);
    var filter = $("#search_input").val().toUpperCase();
    var divs = $(".options_list_on_seacrh");
    var names = [];
    for(var i = 0; i< divs.length; i++)
    {
        console.log($(divs[i]).find('img').attr('name').toUpperCase().indexOf(filter));
       if($(divs[i]).find('img').attr('name').toUpperCase().indexOf(filter) < 0)
        {
            $(divs[i]).hide();
        }
        else
        {
            $(divs[i]).show();
        }
    }

}

function onChange(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {   //event for the end of load
        $('#img').attr('src', e.target.result);
    };
  
    reader.readAsDataURL(file);
  }