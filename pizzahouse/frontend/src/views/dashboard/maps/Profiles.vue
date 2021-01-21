<template>
  <v-container id="profile" fluid tag="section">
    <v-data-table
    :headers="headers"
    :items="profiles"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>profils d'utilisateur</v-toolbar-title>
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
                      v-model="editedItem.profile_lasttname"
                      label="Nom utilisateur"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.profile_firstname"
                      label="Prénom utilisateur"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4">
                    <v-text-field
                      v-model="editedItem.profile_pseudo"
                      label="Pseudo utilisateur"
                    ></v-text-field>
                  </v-col>
                   <v-col
                    cols="12"
                    sm="6"
                    md="4">
                    <v-text-field
                      v-model="editedItem.profile_password"
                      type="password"
                      label="Mot de passe"
                    ></v-text-field>
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
            <v-card-title class="headline">Etes vous sur de vouloir supprimer ce profile?</v-card-title>
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
  name: 'profile',
  data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {text: 'profile_id', value: 'profile_id'},
        {text: 'profile_lasttname', value: 'profile_lasttname'},
        {text: 'profile_firstname', value: 'profile_firstname'},
        {text: 'profile_pseudo', value: 'profile_pseudo'},
        {text: 'profile_password', value: 'profile_password'},
        { text: 'Actions', value: 'actions'},
      ],
      profiles: [],
      editedIndex: -1,
      editedItem: {
        profile_id: '',
        profile_lasttname: '',
        profile_firstname: '',
        profile_pseudo: '',
        profile_password: '',
      },
      defaultItem: {
        profile_id: '',
        profile_lasttname: '',
        profile_firstname: '',
        profile_pseudo: '',
        profile_password: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Nouveau profile' : 'Modifier profile'
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
      getItem() {
      axios.get('http://127.0.0.1:8000/api/profiles/').then((response) => {
        this.profiles= response.data;
      });
    },
      editItem (item) {
        this.editedIndex = this.profiles.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true;
        axios.put('http://127.0.0.1:8000/api/profiles/'+item.profile_id+'/')
          .then(response => {
            console.log(response);
    })
      },

      deleteItem (item) {
        console.log(item);
        this.editedIndex = this.profiles.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
        axios.delete('http://127.0.0.1:8000/api/profiles/'+item.profile_id)
            .then(response=>{
              console.log(response);
            })
      },

      deleteItemConfirm () {
        this.profiles.splice(this.editedIndex, 1)
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
          axios.put('http://127.0.0.1:8000/api/profiles/'+this.editedItem.profile_id+'/',{
            profile_lasttname: this.editedItem.profile_lasttname, profile_firstname: this.editedItem.profile_firstname, 
            profile_pseudo: this.editedItem.profile_pseudo, profile_password: this.editedItem.profile_password})
            .then(response=>{
              console.log('response:'+response);
            })
          Object.assign(this.profiles[this.editedIndex], this.editedItem)
        } else {
          axios.post('http://127.0.0.1:8000/api/profiles/',{profile_id: this.editedItem.profile_id, profile_lasttname: this.editedItem.profile_lasttname, profile_firstname: this.editedItem.profile_firstname, 
            profile_pseudo: this.editedItem.profile_pseudo, profile_password: this.editedItem.profile_password})
           .then(function (response) {
              console.log(response);
          })
           .catch(function (error) {
              console.log(error);
          });
          this.profiles.push(this.editedItem)
        }
        this.close()
      },
    },
}
</script>
