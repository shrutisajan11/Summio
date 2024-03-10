<!-- Add this at the end of your HTML files, just before the closing </body> tag -->

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>

<script>
  // Wait for the DOM to be ready
  $(document).ready(function () {

    // Navbar functionality
    $('.nl').on('click', function (e) {
      e.preventDefault(); // Prevent default behavior of the link
      var page = $(this).attr('href');
      window.location.href = page; // Redirect to the clicked page
    });

    $('.n1').on('click', function (e) {
      e.preventDefault();
      var page = $(this).attr('href');
      window.location.href = page;
    });

    // Form submission
    $('form').submit(function (e) {
      e.preventDefault(); // Prevent the default form submission
      var youtubeUrl = $('input[name="youtube_url"]').val();

      // Add your logic for handling the form data (e.g., sending an AJAX request)

      // For now, let's just log the YouTube URL to the console
      console.log("YouTube URL:", youtubeUrl);
    });

    // Button click functionality
    $('.sum').on('click', function () {
      // Add your logic for the button click event
      console.log("Summarize button clicked!");
    });

  });
</script>
