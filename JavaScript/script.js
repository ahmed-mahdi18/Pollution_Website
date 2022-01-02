var firebaseConfig = {
    apiKey: "AIzaSyC9HPObbRnxjtFmn9jqZNSPPkJl4m6CGtw",
    authDomain: "lc-project-26ac3.firebaseapp.com",
    databaseURL: "https://lc-project-26ac3.firebaseio.com",
    projectId: "lc-project-26ac3",
    storageBucket: "lc-project-26ac3.appspot.com",
    messagingSenderId: "17316483154",
    appId: "1:17316483154:web:ce11235d00cff9cd1c0f8b"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
 

  function writeData(){
    var nameVar = document.getElementById('name').value;
	  var surnameVar = document.getElementById('surname').value;
		var emailVar = document.getElementById('email').value;
		var contactVar = document.getElementById('contact').value;
		var messageVar = document.getElementById('message').value;


	  var myDBconn = firebase.database().ref();
	  var myDataLoc= myDBconn.child('Ahmedsdata/Messages');
	  var data = myDataLoc.push();

		//show alert
document.querySelector('#alert').style.display = 'block';

//hide alert after 3 seconds
setTimeout(function(){
  document.querySelector('#alert').style.display = 'none';
},3000);
  


	  data.set(
		{
			name:nameVar,
			surname:surnameVar,
			email: emailVar,
			contact: contactVar,
      message: messageVar,
		  
		}
  );
    
		document.getElementById('name').value = "";
    document.getElementById('surname').value = "";
		document.getElementById('email').value = "";
		document.getElementById('contact').value = "";
		document.getElementById('message').value = "";
}



