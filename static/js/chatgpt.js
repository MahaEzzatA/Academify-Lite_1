$(document).ready(function() {
            // Send the form on enter keypress and avoid if shift is pressed
            $('#prompt').keypress(function(event) {
                if (event.keyCode === 13 && !event.shiftKey) {
                    event.preventDefault();
                    $('form').submit();
                }
            });
            var copy_icon_source =   "static/img/1827973.png";
            var twitter_icon_source = "static/img/5969020.png";
            tbl =  document.getElementById("tbl");
            $('form').on('submit', function(event) {
                event.preventDefault();
            // get the CSRF token from the cookie
            var csrftoken = Cookies.get('csrftoken');

            // set the CSRF token in the AJAX headers
            $.ajaxSetup({
                headers: { 'X-CSRFToken': csrftoken }
            });
                // Get the prompt
                var prompt = $('#prompt').val();
                //var dateTime = new Date();
                //var time = dateTime.toLocaleTimeString();
                $('#response').text('');
                while (tbl.hasChildNodes()) {
                    tbl.removeChild(tbl.lastChild);
                }
                // Add the prompt to the response div
                $('#response').append('<p <i class="bi bi-person"></i>: ' + prompt + '</p>');
                //$('#response #GFG1').css({"color": "green", "width": "90%", "float": "left"});
                // Clear the prompt
                $('#prompt').val('');
                $.ajax({
                    url: '/',
                    type: 'POST',
                    data: {prompt: ' """ '+ prompt + ' """ ' },
                    dataType: 'json',
                    success: function(data) {
                        //$('#tweet').append('<p id="GFG2">('+ time + ') <i class="bi bi-robot"></i>: ' + data.response + '</p>');
                        array = data.response.split(/\r?\n|\r|\n/g);
                        if (array.length > 1){
                            for(i in array){
                                array[i] = array[i].replace(/\d+\-/g, '');
                                if((array[i].length > 0 )&&(array[i].trim().length !== 0)){
                                    build_table_row(tbl,copy_icon_source,twitter_icon_source, array[i]);
                                }
                            }
                        }
                        else{
                            const row = tbl.insertRow();
                            const cell1 = row.insertCell(0);
                            cell1.style.width = '100%';
                            cell1.textContent = array[0];
                        }
                        //$('#response #GFG2').css({"color": "red", "width": "90%", "float": "right"});

                        $('#tweet').append(tbl)
                    }
                });
            });
        });
            // Function to share text on Twitter
            function shareOnTwitter(content) {
                var tweetUrl = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(content);
                window.open(tweetUrl, '_blank');
            }
            // Function to copy text to clipboard
            function copyTextToClipboard(content) {
                navigator.clipboard.writeText(content);
            }
            function build_table_row(tbl, copy_icon, twitter_icon, post_content) {
                const row = tbl.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                const cell3 = row.insertCell(2);

                cell1.textContent = post_content;
                create_row_btn(copy_icon, cell2, post_content, "copy");
                create_row_btn(twitter_icon, cell3, post_content, "share");
            }
            function create_row_btn(icon_source, cell, post_content, flag) {
                var btn = document.createElement('span');
                btn.innerHTML = "<span class='u-border-none u-btn u-button-style u-none u-text-palette-2-base u-btn-2'></span>";
                btn.style = "cursor:pointer;";
                icon = create_icon(icon_source);
                if (flag == "copy") {
                        btn.title = "Copy";
                        btn.addEventListener('click', () => {copyTextToClipboard(post_content);});
                } else {
                        btn.title = "Share on X";
                        btn.addEventListener('click', () => {shareOnTwitter(post_content);});
                }
                btn.append(icon);
                cell.appendChild(btn);
            }
            function create_icon(icon_source) {
                let img = document.createElement('img');
                img.src = icon_source;
                img.style.height = '50px';
                img.style.width = '50px';
                return img;
            }

