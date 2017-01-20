<!-- Left side column. contains the logo and sidebar -->
  <aside class="main-sidebar">
    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar">
      <!-- Sidebar user panel -->
      <div class="user-panel">
        <div class="pull-left image">
          <img src="dist/img/user2-160x160.jpg" class="img-circle" alt="User Image">
        </div>
        <div class="pull-left info">
          <p>Alexander Pierce</p>
          <a href="#"><i class="fa fa-circle text-success"></i> Online</a>
        </div>
      </div>
      <!-- search form -->
      <form action="#" method="get" class="sidebar-form">
        <div class="input-group">
          <input type="text" name="q" class="form-control" placeholder="Search...">
              <span class="input-group-btn">
                <button type="submit" name="search" id="search-btn" class="btn btn-flat"><i class="fa fa-search"></i>
                </button>
              </span>
        </div>
      </form>
      <!-- /.search form -->
      <!-- sidebar menu: : style can be found in sidebar.less -->
      <ul class="sidebar-menu">
        <li class="header">MAIN NAVIGATION</li>
        <?php if ($hide_menu != true) {
  

                  // mymenu::hello("world");
                  
                  $menu = mymenu::find_all_parent();


                  // print_r($menu);
                  $op = "";
                  $main_active = "";
                  $sidebar_active_id = $_GET['position'];
                  $sidebar_active= mymenu::find_by_id($sidebar_active_id);
// echo "<script>alert('Here is error');</script>";
                  if(!is_null($sidebar_active->parent_id)){
                    $main_active = mymenu::find_by_id($sidebar_active->parent_id);
                  }
                  
                  foreach ($menu as $item) {
                    if ($item->id == 0) {
                      continue;
                    }
                    $aditem = "";
                    $subs = mymenu::find_children($item->id);

                    if (count($subs) !=0){
                      if($main_active->id == $item->id){
                        $aditem = "class = \"active\" ";
                      }

                      $op .= "<li class =\"treeview\"> 
                        <a {$aditem} href=\"#\">
                          <i class=\"fa ". $item->icon." \"></i><span>".
                          $item->nepl_name .
                          "</span>
                        </a>";
                      

                      $op .= "<ul class=\"treeview-menu\">";
                      $aditem = "";
                      $adsub = "";
                      foreach ($subs as $sub_item) {
                        if ($sub_item->id == $sidebar_active->id){
                          $adsub = "class =\"active\"";
                        }

                        $op .= "<li {$adsub}>";
                        $op .= "<a href=\"". $sub_item->href ;
                        if(strpos($sub_item->href, "?") == NULL){
                          $op .= "?position=". $sub_item->id;
                        }else{
                          $op .= "&position=". $sub_item->id;
                        }
                        $op .= "\">";
                        $op .=  "<i class=\"{$sub_item->icon}\"></i>" .$sub_item->nepl_name." </a></li>";
                        $adsub = "";
                      }
                        
                      $op .= "</ul>";
                      $op .= "</li>";

                      
                      
                    } else{
//Checking the Active Menu
                      if ($sidebar_active_id==$item->id) { 
                        $aditem = "class = \"active\""; 
                      }
                      $op .= "<li class=\"mt\">
                      <a {$aditem} href=\"".$item->href."\">
                          <i class=\"fa ".$item->icon. "\"></i>
                          <span>".$item->nepl_name."</span>
                      </a>
                  </li>";
                    }                  

                  }

                  echo $op;

                   ?>

              </ul>
              <?php
} //print_r($sub_item); ?>

<!--         <li class="active treeview">
          <a href="#">
            <i class="fa fa-dashboard"></i> <span>Dashboard</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li class="active"><a href="index.html"><i class="fa fa-circle-o"></i> Dashboard v1</a></li>
            <li><a href="index2.html"><i class="fa fa-circle-o"></i> Dashboard v2</a></li>
          </ul>
        </li>
        <li class="treeview">
          <a href="#">
            <i class="fa fa-files-o"></i>
            <span>Layout Options</span>
            <span class="pull-right-container">
              <span class="label label-primary pull-right">4</span>
            </span>
          </a>
          <ul class="treeview-menu">
            <li><a href="pages/layout/top-nav.html"><i class="fa fa-circle-o"></i> Top Navigation</a></li>
            <li><a href="pages/layout/boxed.html"><i class="fa fa-circle-o"></i> Boxed</a></li>
            <li><a href="pages/layout/fixed.html"><i class="fa fa-circle-o"></i> Fixed</a></li>
            <li><a href="pages/layout/collapsed-sidebar.html"><i class="fa fa-circle-o"></i> Collapsed Sidebar</a></li>
          </ul>
        </li>
        <li>
          <a href="pages/calendar.html">
            <i class="fa fa-calendar"></i> <span>Calendar</span>
            <span class="pull-right-container">
              <small class="label pull-right bg-red">3</small>
              <small class="label pull-right bg-blue">17</small>
            </span>
          </a>
        </li> -->
    </section>
  </aside>