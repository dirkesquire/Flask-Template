RestJS is a JS library that makes it super easy to use knockout via Rest.
AJAX calls can be made in one line of code, with minimal fuss.

To get this working add the following files to your project:

1) Define a models.js in your own project with custom fields
FILE: YourProject/wwwroot/js/models.js:

    function Model() {
        var self = this;
        self.id = ko.observable();                  //int
        self.name = ko.observable();                //string
    }

    function Kind() {
        var self = this;
        self.id = ko.observable();                  //int
        self.name = ko.observable();                //string
    }

    function Entity() {
        var self = this;
        self.id = ko.observable();                  //int
        self.name = ko.observable();                //string
    }

2) Setup Your URLS:
FILE: YourProject/wwwroot/js/site.js:

    function Repository() {
        var self = this;
        self.urls = {
            root: '/api',
            models: '/api/Model',
            kinds: '/api/Kind',
            entities: '/api/Entity',
        };

        self.Models = new BaseController(self.urls.models, Model);
        self.Kinds = new BaseController(self.urls.kinds, Kind);
        self.Entities = new BaseController(self.urls.entities, Entities);
        self.delay = Delay;
    }

    window.API = new Repository();

    // Optional:
    // You can inherit from BaseController in your own project in order to add custom methods:
    function MyFancyController(baseUrl, typeFn) {
        BaseController.call(this, baseUrl, typeFn);
        var self = this;

        self.loadSpecial = function(a,b,c) {
            //Custom ajax function
        }
    }

3) Now define, your knockout viewmodels. Typically one of these per page view:
FILE: YourProject/wwwroot/js/pageview.js:

// To get
Typically you would write one view.js for each webpage

function PageViewModel() {
    var self = this;
    self.models = ko.observableArray();

    // Get All:
    //The data at window.API.urls.models are fetched and stored in self.models knockout observableArray:
    window.API.Models.load(self.models).then(
        (data) => { console.log('data: ', data); },
        (error) => { console.log('error: ', error); }
    )

    //Example of fetching a single item directly from the API
    window.API.Models.fetchById(1).then(
        (a) => {
            console.log('account: ', a);
            self.accounts.push(a);
        },
        (error) => { coonsole.log('error: ', error); }
    );

    //Save example:
    self.saveClick = (item) => {
        var isNew = item.id() == null;
        window.API.Items.save(item.id(), item).then(
            (data) => {
                if (isNew) {
                    item.id(data.id);
                    self.items.push(item); //If id was empty - we need to add it to the collection after saving.
                }
            },
            (error) => { }
        );
    };

    //Delete example:
    self.deleteClick = (item) => {
        var result = confirm('Are you sure you wish to delete this item?');
        if (!result) return;
        window.API.Items.delete(item.id()).then(
            (result) => {
                self.items.remove(item);
            },
            (error) => { }
        );
    };


    //Example of Delay function usage:
    window.API.delay(500).then(function() {
        // Do Something...
    });
}

$().ready(function () {
    var vm = new PageViewModel()
    $('.ko-view-mypage').each( (index, element) => ko.applyBindings(vm, element) );
});