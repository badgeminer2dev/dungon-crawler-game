<script>
// When the user clicks on <div>, open the popup
function showNotification() {
  if(window.Notification && Notification.permission !== "denied") {
	Notification.requestPermission(function(status) {  // status is "granted", if accepted by user
		var n = new Notification('Title', { 
			body: 'I am the body text!',
			icon: '/path/to/icon.png' // optional
		}); 
	});
 };
}
</script>
<p><button onclick="showNotification()">Show a Notification</button></p>
