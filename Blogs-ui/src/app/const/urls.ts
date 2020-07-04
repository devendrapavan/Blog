
export class Urls {
    private static readonly HOST = "http://192.168.0.106:8000";
    public static readonly LOGIN = Urls.HOST + '/login/';
    public static readonly ALLBLOGS = Urls.HOST + '/dashboard/get-blogs/';
    public static readonly CREATE = Urls.HOST + '/dashboard/create-article/';
    public static readonly UPDATE = Urls.HOST + '/dashboard/update-article/';
    public static readonly ARTICLEDETAILS = Urls.HOST + '/dashboard/article-by-id/';
    // private static readonly SERVER_HOST = Config.API_HOST;
}