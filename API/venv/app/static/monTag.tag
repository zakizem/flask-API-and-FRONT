<montag>
  <%-- Aller retour avec le serveur, création de la page --%>
{ items }
    <ul>
      <li each={ items }>
        <div>
          alo

        </div>
        { title }
      </li>
    </ul>
    { response }d
    <ul>
      <li each={ response }>
        <div>
          alo

        </div>
        { title }
      </li>
    </ul>


    <button class="btn btn-primary" onclick={ httpGet('http://127.0.0.1:5000/1') }>
      Valider</button>



    <script>
      this.items = [
        {
          title: 'First item',
          done: true
        }, {
          title: 'Second item'
        }, {
          title: 'Third item'
        }
      ]


      this.ikaz='alal'
      var self=this
      this.response={contenu:'rien du tout'}
      console.log('response avant : '+JSON.stringify(this.response));


      httpGet(theurl) {
        return function (e) {
          alert('ola')

          self.ikaz='hee'
          var xmlHttp = new XMLHttpRequest();


          xmlHttp.open("GET", theurl, true); // false for synchronous request
          xmlHttp.send(null);

          xmlHttp.onreadystatechange = function () { //Call a function when the state changes.

            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {

              self.response = JSON.parse(xmlHttp.responseText);


              // response = xmlHttp.responseText;
              console.log('response');
              alert(self.response);
              console.log(self.response);
              console.log(theurl);

              return self.response;
            }
          }
        }
      }

      ibel(){return function (e) {return 'aloa';}}
      console.log('ibel : '+self.ibel()()+' \nself.resultat: ' + self.httpGet('http://127.0.0.1:5000/1')()+'\nréponse : '+ JSON.stringify(self.response)+'\nthis.ikaz : '+self.ikaz);

        setTimeout(function () {
          console.log('ibel : '+self.ibel()()+' \nself.resultat: ' + self.httpGet('http://127.0.0.1:5000/1')()+'\nréponse : '+ JSON.stringify(self.response)+'\nthis.ikaz : '+self.ikaz);
        }, 2000);

      // this.test = this.httpGet('http://127.0.0.1:5000/1')();
    </script>

</montag>
