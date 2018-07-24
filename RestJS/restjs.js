function BaseController(baseUrl, typeFn) {
    var self = this;
    self.baseUrl = baseUrl;
    self.typeFn = typeFn;
    self.all = ko.observableArray();

    self.paged = ko.observableArray();
    self.skip = 0;
    self.pageLength = 25;

    self.mapping = { create: function (options) { return ko.mapping.fromJS(options.data, {}, new typeFn()); } };

    //Fetches a list of items, and optionally maps result to ko.observableArray (if provided)
    self.load = function(observableArray) {
        return new Promise(function (resolve, reject) {
            if (self.baseUrl == null) {
                reject('BaseUrl should not be null');
                return;
            }
            $.getJSON(self.baseUrl, function (data) {
                ko.mapping.fromJS(data, self.mapping, self.all);
                if (observableArray != null) observableArray(self.all());
                resolve(self.all());
            }).fail(reject);
        });
    };

    self.findById = function (id) {
        return ko.utils.arrayFirst(self.all(), function (o) {
            return o.id() == id;
        });
    };

    self.fetchById = function (id, observable) {
        return new Promise(function (resolve, reject) {
            $.getJSON(self.baseUrl + '/' + id, function (data) {
                var o = ko.mapping.fromJS(data, {}, new typeFn());
                if (observable != null) observable(o);
                resolve(o);
            }).fail(reject);
        });
    };

    self.save = function(id, item, observable) {
        //To exclude some properties create a mapping:
        //var mapping = {'ignore': ["myProperty"] }
        //var viewModel = ko.mapping.toJS(item, mapping);

        o = ko.mapping.toJS(item);
        var data = JSON.stringify(o);

        return new Promise(function (resolve, reject) {
            if (id == null) {
                $.ajax({type: "POST", url: self.baseUrl, contentType: "application/json", processData: false, data: data})
                .done(function (data) {
                    resolve(data);
                }).fail(reject);

            }
            else {
                $.put(self.baseUrl + (self.baseUrl.endsWith('/') ? '' : '/') + id, data, null, 'application/json')
                .done(function (data) {
                    resolve(data);
                }).fail(reject);
            }
        });
    };

    self.delete = function(id) {
        return new Promise(function (resolve, reject) {
            $.delete(self.baseUrl + (self.baseUrl.endsWith('/') ? '' : '/') + id).done(resolve).fail(reject);
        });
    };
}

//Jquery POST/DELETE
jQuery.each( [ "put", "delete" ], function( i, method ) {
    jQuery[ method ] = function( url, data, callback, type ) {
      if ( jQuery.isFunction( data ) ) {
        type = type || callback;
        callback = data;
        data = undefined;
      }

      return jQuery.ajax({
        url: url,
        type: method,
        contentType: type,
        data: data,
        success: callback
      });
    };
  });

function Delay(ms) {
  return new Promise(function(resolve, reject) {
      setTimeout(function() { resolve(); }, ms);
  });
}