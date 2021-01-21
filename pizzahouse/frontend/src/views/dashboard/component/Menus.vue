<template>
  <v-container id="menu" fluid tag="section">
    <v-data-table
    :headers="headers"
    :items="Menus"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Menus</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Ajouter 
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.menu_name"
                      label="Nom Menu"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-textarea
                      v-model="editedItem.menu_body"
                      label="Description Menu"
                    ></v-textarea>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4">
                    <input type="file" accept="image/*" @change="uploadImage($event)" id="menu_img">
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Annuler
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Sauvegarder
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Etes vous sur de vouloir supprimer ce menu?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Annuler</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="initialize"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
  </v-container>
</template>
<script>
  import axios from 'axios';
  export default {
  name: 'menu',
  data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {text: 'menu_id', value: 'menu_id'},
        { text: 'menu_name', value: 'menu_name'},
        {text: 'menu_body', value: 'menu_body'},
        {text: 'menu_img', value: 'menu_img'},
        { text: 'Actions', value: 'actions'},
      ],
      Menus: [],
      editedIndex: -1,
      editedItem: {
        menu_id: '',
        menu_name: '',
        menu_body: '',
        menu_img: '',
      },
      defaultItem: {
        menu_id: '',
        menu_name: '',
        menu_body: '',
        menu_img: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Nouveau menu' : 'Modifier menu'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.getItem();
    },

    methods: {
      uploadImage(event) {
        const URL = 'E:\TOSHIBA\SITW\Doctorat\Thème\pics'; 
        let data = new FormData();
        data.append('name', 'my-picture');
        data.append('file', event.target.files[0]); 
    let config = {
      header : {
        'Content-Type' : 'image/png'
      }
    }
    axios.put(
      URL, 
      data,
      config
    ).then(
      response => {
        console.log('image upload response > ', response)
      }
    )
  },
      getItem() {
      axios.get('http://127.0.0.1:8000/api/Menus/').then((response) => {
        this.Menus= response.data;
      });
    },
      editItem (item) {
        this.editedIndex = this.Menus.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true;
        axios.put('http://127.0.0.1:8000/api/Menus/'+item.menu_id+'/')
          .then(response => {
            console.log(response);
    })
      },

      deleteItem (item) {
        console.log(item);
        this.editedIndex = this.Menus.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        axios.delete('http://127.0.0.1:8000/api/Menus/'+item.menu_id)
            .then(response=>{
              console.log(response);
            })
      },

      deleteItemConfirm () {
        this.Menus.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          console.log(this.editedItem);
          axios.put('http://127.0.0.1:8000/api/Menus/'+this.editedItem.menu_id+'/',{
            menu_name: this.editedItem.menu_name})
            .then(response=>{
              console.log('response:'+response);
            })
          Object.assign(this.Menus[this.editedIndex], this.editedItem)
        } else {
          axios.post('http://127.0.0.1:8000/api/Menus/',{menu_id: this.editedItem.menu_id, menu_name: this.editedItem.menu_name})
           .then(function (response) {
              console.log(response);
          })
           .catch(function (error) {
              console.log(error);
          });
          this.Menus.push(this.editedItem)
        }
        this.close()
      },
    },
}
</script>
