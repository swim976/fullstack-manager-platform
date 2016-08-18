var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    sass = require('gulp-ruby-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    browserify = require('gulp-browserify'),
    jshint = require('gulp-jshint'),
    minifyCss = require('gulp-minify-css'),
    notify = require('gulp-notify');
    // browserSync = require('browser-sync').create();

var DEST = 'dashboard/static';

gulp.task('move-js', function(){
    return gulp.src([
            'node_modules/gentelella/vendors/*/*.min.js',
            'node_modules/gentelella/vendors/*/dist/*.min.js',
            'node_modules/gentelella/vendors/*/dist/js/*.min.js',
            'node_modules/gentelella/vendors/*/js/*.min.js',
        ], {base: './node_modules/gentelella/vendors'}).pipe(gulp.dest(DEST + '/js'))
});

// gulp.task('scripts', function(){
//     gulp.src('gentelella/vendors/*/*.min.js')
//         .pipe(bro)
//     gulp.src('dashboard/src/js/base.js')
//             .pipe(browserify({
//                 insertGlobals: true,
//                 debug: !gulp.env.production
//             }))
//             .pipe(concat('base.js'))        // 这是把上面所有的js文件合并为一个文件
//             .pipe(gulp.dest(DEST+'/js'))
//             .pipe(rename({suffix: '.min'}))
//             .pipe(uglify())
//             .pipe(gulp.dest(DEST+'/js'))
//             .pipe(notify({
//                 message: 'Scripts task complete'
//             }));
//     gulp.src('dashboard/src/js/datatables.js')
//             .pipe(browserify({
//                 insertGlobals: true,
//                 debug: !gulp.env.production
//             }))
//             .pipe(concat('datatables.js'))        // 这是把上面所有的js文件合并为一个文件
//             .pipe(gulp.dest(DEST+'/js'))
//             .pipe(rename({suffix: '.min'}))
//             .pipe(uglify())
//             .pipe(gulp.dest(DEST+'/js'))
//             .pipe(notify({
//                 message: 'Scripts task complete'
//             }));
// });

gulp.task('concat-css', function(){
    gulp.src([
            'node_modules/gentelella/vendors/bootstrap/dist/css/bootstrap.min.css',
            'node_modules/gentelella/vendors/font-awesome/css/font-awesome.min.css',
        ])
        .pipe(concat('base.min.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest(DEST+'/css'));

    gulp.src(['node_modules/gentelella/build/css/custom.css'])
        .pipe(concat('custom.min.css'))
        .pipe(gulp.dest(DEST+'/css'));

    gulp.src(['node_modules/gentelella/vendors/animate.css/animate.min.css'])
        .pipe(concat('animate.min.css'))
        .pipe(gulp.dest(DEST + '/css'));

    gulp.src([
            'node_modules/gentelella/vendors/datatables.net-bs/css/dataTables.bootstrap.min.css',
            'node_modules/gentelella/vendors/datatables.net-buttons-bs/css/buttons.bootstrap.min.css',
            'node_modules/gentelella/vendors/datatables.net-fixedheader-bs/css/fixedHeader.bootstrap.min.css',
            'node_modules/gentelella/vendors/datatables.net-responsive-bs/css/responsive.bootstrap.min.css',
            'node_modules/gentelella/vendors/datatables.net-scroller-bs/css/scroller.bootstrap.min.css',
        ])
        .pipe(concat('datatables.min.css'))
        .pipe(gulp.dest(DEST + '/css'));
});

// gulp.task('default', ['clean'], function(){
//     gulp.start('scripts');
// });

gulp.task('watch', function(){
    gulp.watch('dashboard/src/js/*.js', ['move-js']);
    gulp.watch('dashboard/src/css/*.css', ['concat-css']);
});

gulp.task('default', ['watch']);
