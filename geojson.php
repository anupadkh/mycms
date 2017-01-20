<?php include_once 'formheader.php'; ?>
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <h1>
        GEOJSON लेयर अपलोड
        <small>शाखा</small>
      </h1>
      <ol class="breadcrumb">
        <li><a href="index.php"><i class="fa fa-dashboard"></i> Home</a></li>
        <li><a href="#">Geojson</a></li>
        <li class="active">New Upload</li>
      </ol>
    </section>

    <!-- Main content -->
    <section class="content">
      <div class="row">
        <!-- left column -->
        <div class="col-md-6">
          <!-- general form elements -->
          <div class="box box-primary">
            <div class="box-header with-border">
              <h3 class="box-title">फारम</h3>
              <?php if (isset($_GET[id])) {
                    echo "Alert('Saved')";
              } ?>
            </div>
                   <form role="form" action="uploads/geojson_upload.php" method="POST" enctype="multipart/form-data">
                    <div class="box-body">
                      <div class="form-group">
                        <label for="exampleInputFile">File input</label>
                        <input type="file" id="exampleInputFile" name="filename">

                        <p class="help-block">Please upload your file</p>
                      </div>
                      <div class="form-group">
                        <label for="coordinatesystem">Coordinate System</label>
                        <input type="text" class="form-control" id="coordinatesystem" placeholder="WGS1984" name="cs">
                      </div>
                      <div class="form-group">
                        <label for="correction">Correction Factor</label>
                        <input type="text" class="form-control" id="correction" placeholder="WGS1984" name="correc">
                        <p class="help-block">Latitude and Longitude eg. 83.456,24.569</p>
                      </div>
                      <div class="form-group">
                        <label for="layer">Name for the Geojson File</label>
                        <input type="text" class="form-control" id="layer" placeholder="" name="layername">
                        <p class="help-block">For Future Reference</p>
                      </div>
                      <div class="form-group">
                        <label for="identifier">Identifier Attribut</label>
                        <input type="text" class="form-control" id="identifier" placeholder="" name="identifiername">
                        <p class="help-block">The column Name that holds the name for figure elements</p>
                      </div>
                        
                        <input type="hidden" name="nav_id" value="<?php echo $_GET['id']; ?>" />
                        <input type="hidden" name="nav_table" value="<?php echo $_GET['tab']; ?>" />                  
                        <input type="hidden" name="position" value="<?php echo $_GET['position']; ?>" />

                    <div class="box-footer">
                      <input type="hidden" name="submit">
                      <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                  </div>
                  </form>
          </div>
      </div>
      </div>
      </section>
      </div>
<?php require_once 'footer.php'; ?>
          